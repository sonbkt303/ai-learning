#!/usr/bin/env python3
"""
🧪 Test Script - Kiểm tra môi trường Python
Chạy script này để đảm bảo tất cả thư viện đã được cài đặt đúng.
"""

def test_imports():
    """Test all essential library imports"""
    print("🔍 Testing library imports...")
    
    try:
        import numpy as np
        print("✅ NumPy:", np.__version__)
    except ImportError:
        print("❌ NumPy not installed")
    
    try:
        import pandas as pd
        print("✅ Pandas:", pd.__version__)
    except ImportError:
        print("❌ Pandas not installed")
    
    try:
        import matplotlib
        print("✅ Matplotlib:", matplotlib.__version__)
    except ImportError:
        print("❌ Matplotlib not installed")
    
    try:
        import jupyter
        print("✅ Jupyter installed")
    except ImportError:
        print("❌ Jupyter not installed")
    
    try:
        import seaborn as sns
        print("✅ Seaborn:", sns.__version__)
    except ImportError:
        print("❌ Seaborn not installed")
    
    try:
        import sklearn
        print("✅ Scikit-learn:", sklearn.__version__)
    except ImportError:
        print("❌ Scikit-learn not installed")

def test_basic_operations():
    """Test basic data operations"""
    print("\n🔢 Testing basic operations...")
    
    try:
        import numpy as np
        arr = np.array([1, 2, 3, 4, 5])
        print(f"✅ NumPy array created: {arr}")
        print(f"✅ Array sum: {np.sum(arr)}")
    except Exception as e:
        print(f"❌ NumPy operations failed: {e}")
    
    try:
        import pandas as pd
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        print("✅ Pandas DataFrame created:")
        print(df)
    except Exception as e:
        print(f"❌ Pandas operations failed: {e}")

def main():
    """Main test function"""
    print("🚀 Starting Python Environment Test")
    print("=" * 50)
    
    import sys
    print(f"🐍 Python version: {sys.version}")
    print(f"📁 Python executable: {sys.executable}")
    
    test_imports()
    test_basic_operations()
    
    print("\n" + "=" * 50)
    print("✨ Test completed! Check results above.")
    print("📝 If any library shows ❌, install it with: pip install <library-name>")

if __name__ == "__main__":
    main()