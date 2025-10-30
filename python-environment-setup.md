# 🧰 Hướng Dẫn Setup Môi Trường Luyện Tập Python (Cho Data Analysis & AI)

## 1️⃣ Cài đặt Python
- Tải Python mới nhất: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Khi cài, **tick chọn “Add Python to PATH”**
- Kiểm tra sau khi cài:
  ```bash
  python --version
  ```

---

## 2️⃣ Cài đặt công cụ làm việc (IDE)

### 🔹 Visual Studio Code (VSCode)
- Tải: [https://code.visualstudio.com](https://code.visualstudio.com)
- Extensions cần có:
  - `Python` (Microsoft)
  - `Jupyter` (chạy notebook)
  - `Pylance` (gợi ý code)
  - `Code Runner` (chạy nhanh file)

---

## 3️⃣ Tạo môi trường ảo (Virtual Environment)
Tạo môi trường riêng cho từng project.

Trong thư mục project:
```bash
python -m venv venv
```

Kích hoạt:
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

Khi thành công, terminal sẽ hiển thị `(venv)`.

---

## 4️⃣ Cài thư viện cần thiết
```bash
pip install numpy pandas matplotlib jupyter
```

Tuỳ chọn thêm:
```bash
pip install seaborn scikit-learn
```

---

## 5️⃣ Dùng Jupyter Notebook để thực hành
Cài đặt (nếu chưa có):
```bash
pip install notebook
```

Chạy notebook:
```bash
jupyter notebook
```

Trình duyệt sẽ mở ra → tạo file `.ipynb` → viết code Python và chạy từng cell.

---

## 6️⃣ Tổ chức thư mục project (gợi ý)
```
ai-learning/
├── venv/
├── week3-4-data-analysis/
│   ├── notebooks/
│   │   ├── pandas_intro.ipynb
│   │   └── numpy_exercise.ipynb
│   ├── data/
│   │   └── sales.csv
│   └── README.md
```

---

## 7️⃣ (Tùy chọn) Dùng Kaggle hoặc Google Colab
Nếu không muốn cài local:
- **[Kaggle Notebooks](https://www.kaggle.com/code)** — môi trường sẵn thư viện
- **[Google Colab](https://colab.research.google.com)** — chạy Python trên cloud, dễ chia sẻ
