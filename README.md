# Table Change Log

Created: June 17, 2024 1:09 PM

| Version | Date | Description |
| --- | --- | --- |
| 1.1.0 | 10/05/2024 | • Sửa đổi toàn bộ nội dung doc
• Tiến hành phân tích dựa trên các câu hỏi
    ◦ Xác định dữ liệu trả về từ Query API
    ◦ Xác định thời gian Query API
    ◦ Xác định khối lượng dữ liệu trả về và phạm vi dữ liệu
    ◦ Xác định các bài toán đặt ra
    ◦ Xác định dữ liệu cần trích xuất để xử lý bài toán
• Loại bỏ Data Staging và mô hình ERD thiết kế cho CSDL trong staging
• Thiết kế mô hình ELT với Data Lake và Data Mart |
| 1.2.0 | 13/05/2024 | • Chỉnh sửa doc tập trung vào data của NYSE và NASDAQ
    ◦ Cập nhật khối lượng dữ liệu dựa trên phạm vi dữ liệu
• Tách 4 API thành 2 API và 1 Database lưu dữ liệu từ sec-api.io và Alpha Vantage API for market status (giả lập backend database)
    ◦ Thiết kế Database cho dữ liệu từ sec-api.io và Alpha Vantage API for market status
• Thiết kế lại ELT bổ sung Database mới làm Data Source
• Chỉnh sửa Galaxy Schema
    ◦ Chỉ 1 bảng Dim Companies để tối ưu thời gian truy vấn |
| 1.2.1 | 16/05/2024 | • Xác định các thành phần trong ETL
• Bổ sung thiết kế
    ◦ Thiết kế DAG và Task Flow
    ◦ Thiết kế Job Data Flow
    ◦ BPMN ETL
    ◦ File System |
| 1.2.2 | 28/05/2024 | • Chuyển đổi DW sang DuckDB
• Cập nhật ETL
    ◦ Database -> Data lake -> Data Warehouse
    ◦ Sử dụng timestamp khi cập nhật Database |
| 1.3 | 03/06/2024 | Cấu hình môi trường dự án
• Cài đặt, cấu hình Google Compute Engine
• Cài đặt, cấu hình Hadoop (Single Node) - HDFS, YARN
• Cài đặt, cấu hình Python, PostgreSQL, DuckDB
• Cài đặt, cấu hình Spark trên cụm Hadoop |
| 1.6
 | 7/06/2024 | Khởi tạo chức năng
• ETL cho Database
• ELT cho Data Warehouse
• Tạo các Dag
• Tạo API truy cập Data Warrehouse |
| 1.7  | 14/06/2024 | Khởi chạy dự án
• Khởi chạy Airflow 
• Khởi chạy API |
| 1.8 (Processing) | 15/06/2024 | Thiết kế Dashboard
• Xác định & Thiết kế Dashboard
• Lấy dữ liệu thông qua API
• Tải dữ liệu vào Power BI
• Tạo Dashboard |
| 1.9 (Upcoming) |  |  |

# Link Tài liệu: 
https://anhcuonghuynhnguyen.notion.site/T-i-li-u-d-n-ELT_Pipeline_Stock-v1-8-4f4289c245a647f6a2879ca171ee5b2b?pvs=4 