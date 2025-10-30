# 📊 Data Analysis Roadmap (Weeks 3–4)

## 🎯 Mục tiêu sau 2 tuần
- Thành thạo `Pandas`, `NumPy`, `Matplotlib`
- Biết làm việc với dataset (đọc, lọc, xử lý, tổng hợp)
- Tự vẽ biểu đồ, trực quan hóa dữ liệu
- Làm mini project: **Phân tích dữ liệu thực tế từ Kaggle**

---

## 📅 Tuần 3 – Làm quen với Data Analysis

### 🗓️ Ngày 1: Giới thiệu Data Analysis
**Mục tiêu:** Hiểu Data Analysis là gì và quy trình phân tích dữ liệu.  
**Học:**  
- [Intro to Data Analysis – Kaggle](https://www.kaggle.com/learn/data-cleaning)  
- [Data Analysis in Python for Beginners (YouTube)](https://www.youtube.com/watch?v=r-uOLxNrNk8)  
**Thực hành:**  
- Tìm một file `.csv` (vd: `titanic.csv`)  
- Đọc dữ liệu với `pandas.read_csv` và xem 5 dòng đầu (`.head()`).

---

### 🗓️ Ngày 2: NumPy cơ bản
**Mục tiêu:** Hiểu cách xử lý dữ liệu dạng số (array, vector, matrix).  
**Học:**  
- [Kaggle: Intro to NumPy](https://www.kaggle.com/code/colinmorris/intro-to-numpy)  
- [NumPy Quickstart Docs](https://numpy.org/doc/stable/user/quickstart.html)  
**Thực hành:**  
- Tạo mảng 1D, 2D  
- Tính tổng, trung bình, độ lệch chuẩn (`np.mean`, `np.std`)  
- Thực hành `reshape`, `dot`, `sum(axis=...)`.

---

### 🗓️ Ngày 3–4: Pandas cơ bản
**Mục tiêu:** Làm quen với DataFrame – công cụ chính của data analysis.  
**Học:**  
- [Kaggle: Pandas Course](https://www.kaggle.com/learn/pandas)  
- [Pandas Getting Started Docs](https://pandas.pydata.org/docs/getting_started/index.html)  
**Thực hành:**  
- Đọc file CSV (`pd.read_csv`)  
- Truy cập cột, dòng (`df['column']`, `df.loc[]`)  
- Lọc dữ liệu (`df[df['Age'] > 30]`)  
- Tính toán (`df['Salary'].mean()`, `.value_counts()`).

---

### 🗓️ Ngày 5: Làm sạch dữ liệu (Data Cleaning)
**Mục tiêu:** Xử lý dữ liệu bị thiếu, trùng, sai định dạng.  
**Học:**  
- [Kaggle: Data Cleaning](https://www.kaggle.com/learn/data-cleaning)  
- [Handling Missing Data – Pandas Docs](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html)  
**Thực hành:**  
- Tìm giá trị bị thiếu (`df.isnull().sum()`)  
- Điền hoặc loại bỏ (`fillna`, `dropna`)  
- Chuyển kiểu dữ liệu (`astype`).

---

### 🗓️ Ngày 6–7: Thống kê mô tả & tổng hợp dữ liệu
**Mục tiêu:** Hiểu dữ liệu thông qua thống kê và nhóm dữ liệu.  
**Học:**  
- `df.describe()` – mô tả thống kê  
- `groupby()`, `agg()` – nhóm dữ liệu  
- `pivot_table()`  
**Thực hành:**  
- Phân tích dữ liệu theo giới tính, độ tuổi, quốc gia  
- Tính doanh thu trung bình, tổng số lượng  
- Làm báo cáo nhỏ: “Top 5 sản phẩm bán chạy nhất”.

---

## 📅 Tuần 4 – Visualization & Mini Project

### 🗓️ Ngày 8–9: Data Visualization với Matplotlib
**Mục tiêu:** Biểu diễn dữ liệu trực quan.  
**Học:**  
- [Kaggle: Data Visualization](https://www.kaggle.com/learn/data-visualization)  
- [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)  
**Thực hành:**  
- Vẽ biểu đồ cột, đường, tròn (`plt.bar`, `plt.plot`, `plt.pie`)  
- Tùy chỉnh tiêu đề, màu, trục  
- Lưu biểu đồ thành ảnh.

---

### 🗓️ Ngày 10–11: Visualization nâng cao với Seaborn
**Mục tiêu:** Làm biểu đồ đẹp và dễ hiểu.  
**Học:**  
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)  
- Biểu đồ thường dùng:  
  - `sns.histplot`, `sns.boxplot`, `sns.heatmap`, `sns.scatterplot`  
**Thực hành:**  
- Biểu diễn mối quan hệ giữa 2 biến (vd: giá nhà vs diện tích)  
- Tạo biểu đồ heatmap thể hiện correlation.

---

### 🗓️ Ngày 12–13: Mini Project
**Dự án:** *Exploratory Data Analysis (EDA)*  
Chọn một dataset thật từ Kaggle:  
- [Titanic Dataset](https://www.kaggle.com/c/titanic)  
- [Netflix Movies](https://www.kaggle.com/datasets/shivamb/netflix-shows)  
- [Sales Data](https://www.kaggle.com/datasets)

**Mục tiêu:**  
- Làm sạch dữ liệu  
- Phân tích mô tả  
- Vẽ biểu đồ (histogram, pie, correlation heatmap)  
- Rút ra insight.

---

### 🗓️ Ngày 14: Tổng kết & Portfolio
**Mục tiêu:** Tạo báo cáo kết quả và đăng GitHub.  
**Làm:**  
- Xuất notebook thành `.ipynb`  
- Viết `README.md` mô tả dataset và insight chính  
- Commit lên GitHub (`data-analysis-project`).

---

## 📚 Tổng hợp tài liệu

| Mục tiêu | Nguồn học | Loại |
|:----------|:-----------|:------|
| Pandas | [Kaggle Pandas Course](https://www.kaggle.com/learn/pandas) | Free Course |
| NumPy | [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html) | Docs |
| Visualization | [Kaggle Data Visualization](https://www.kaggle.com/learn/data-visualization) | Free Course |
| Cleaning | [Kaggle Data Cleaning](https://www.kaggle.com/learn/data-cleaning) | Free Course |
| EDA practice | [Titanic Dataset](https://www.kaggle.com/c/titanic) | Dataset |

---

## 🧩 Kết quả đạt được
✅ Hiểu quy trình phân tích dữ liệu  
✅ Thành thạo `Pandas`, `NumPy`, `Matplotlib`, `Seaborn`  
✅ Có project đầu tiên về EDA  
✅ Chuẩn bị sẵn kỹ năng bước vào học Machine Learning  
