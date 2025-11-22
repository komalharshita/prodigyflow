import pandas as pd
import os
import google.generativeai as genai

# Initialize Gemini client
# Note: Ensure GEMINI_API_KEY is set in your environment variables
try:
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        print("Gemini client initialized successfully.")
    else:
        print("Warning: GEMINI_API_KEY not found in environment variables. LLM features will be disabled.")
        model = None
except Exception as e:
    print(f"Warning: Gemini client could not be initialized. Error: {e}")
    model = None

def load_data(filepath):
    """Loads data from a CSV file."""
    try:
        df = pd.read_csv(filepath)
        print(f"Successfully loaded data from {filepath}")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def save_data(df, filepath):
    """Saves the DataFrame to a CSV file."""
    try:
        df.to_csv(filepath, index=False)
        print(f"Successfully saved cleaned data to {filepath}")
    except Exception as e:
        print(f"Error saving data: {e}")

def clean_missing(df, strategy='ffill'):
    """
    Handle missing values.
    Strategies: 'ffill', 'bfill', 'drop', 'mean', 'median', 'mode'
    """
    print(f"Executing clean_missing with strategy: {strategy}")
    if strategy == 'ffill':
        return df.ffill()
    elif strategy == 'bfill':
        return df.bfill()
    elif strategy == 'drop':
        return df.dropna()
    elif strategy == 'mean':
        return df.fillna(df.mean(numeric_only=True))
    elif strategy == 'median':
        return df.fillna(df.median(numeric_only=True))
    elif strategy == 'mode':
        return df.fillna(df.mode().iloc[0])
    else:
        print(f"Unknown strategy '{strategy}', defaulting to ffill")
        return df.ffill()

def clean_duplicates(df, keep='first'):
    """Removes duplicate rows."""
    print(f"Executing clean_duplicates keeping: {keep}")
    return df.drop_duplicates(keep=keep)

def clean_text(df):
    """Standardizes text columns (strip whitespace, lowercase)."""
    print("Executing clean_text")
    for col in df.select_dtypes(include='object'):
        df[col] = df[col].str.strip().str.lower()
    return df

def fix_dtypes(df):
    """Infers better data types for columns."""
    print("Executing fix_dtypes")
    return df.infer_objects()

def get_cleaning_plan(df_head_str, user_prompt):
    """Uses Gemini to suggest a cleaning plan based on data sample and user request."""
    if not model:
        return "missing, duplicate, text, datatype" # Fallback default plan

    system_prompt = """You are a data-cleaning agent. 
    Analyze the provided data sample and user request.
    Return a comma-separated list of cleaning steps to apply.
    Available steps: 'missing', 'duplicate', 'text', 'datatype'.
    Example output: missing, text
    """
    
    content = f"{system_prompt}\n\nData Sample:\n{df_head_str}\n\nUser Request: {user_prompt}"

    try:
        response = model.generate_content(content)
        return response.text.strip()
    except Exception as e:
        print(f"Error getting plan from LLM: {e}")
        return "missing, duplicate, text, datatype"

def clean_dataset(df, plan):
    """Applies cleaning functions based on the plan."""
    plan = plan.lower()
    
    if "missing" in plan:
        # Simple heuristic: if numeric, use mean, else ffill
        # For now, defaulting to ffill/bfill as per original or user preference could be added
        df = clean_missing(df) 
    if "duplicate" in plan:
        df = clean_duplicates(df)
    if "text" in plan:
        df = clean_text(df)
    if "datatype" in plan:
        df = fix_dtypes(df)
    
    return df

def analyze_data(df):
    """Prints basic analysis of the dataset."""
    print("\n--- Data Analysis ---")
    print(f"Shape: {df.shape}")
    print(f"Missing Values:\n{df.isnull().sum()}")
    print(f"Duplicates: {df.duplicated().sum()}")
    print("---------------------\n")

def main():
    input_file = "data//data_science_student_marks.csv"
    output_file = "cleaned_data.csv"
    
    print("--- Data Cleaning Agent (Gemini Powered) ---")
    df = load_data(input_file)
    
    if df is not None:
        analyze_data(df)
        
        user_prompt = "Clean this dataset automatically." # Default prompt
        # In a real interactive CLI, we would ask: input("Enter your cleaning goal: ")
        
        print("Generating cleaning plan...")
        plan = get_cleaning_plan(df.head().to_string(), user_prompt)
        print(f"Proposed Plan: {plan}")
        
        # In interactive mode, we would ask for confirmation here.
        print("Applying plan...")
        cleaned_df = clean_dataset(df, plan)
        
        analyze_data(cleaned_df)
        
        save_data(cleaned_df, output_file)
        print("Done.")

if __name__ == "__main__":
    main()
