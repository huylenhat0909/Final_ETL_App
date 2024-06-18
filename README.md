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

# Chương 1: DESIGN

Created: June 17, 2024 1:09 PM

## A. Data Source là gì ?

Data Source là các API do các tổ chức chuyên cung cấp dữ liệu cho thị trường tài chính. Dưới đây là một số API được sử dụng trong dự án:

1. **sec-api.io**:
    - API này giúp chúng ta truy xuất danh sách các công ty hiện đang có mặt trên các thị trường chứng khoán Nyse, Nasdaq.
    - Thông tin chi tiết: [sec-api.io/docs/mapping-api/list-companies-by-exchange](https://sec-api.io/docs/mapping-api/list-companies-by-exchange)
2. **Alpha Vantage**
    1. **API for market status**:
        - API này cung cấp thông tin về các thị trường chứng khoán trên toàn thế giới.
        - Thông tin chi tiết: [alphavantage.co/documentation/#market-status](https://www.alphavantage.co/documentation/#market-status)
    2. **API for news sentiment**:
        - API này cung cấp dữ liệu tin tức thị trường cùng với dữ liệu sentiment từ các nguồn tin hàng đầu.
        - Thông tin chi tiết: [alphavantage.co/documentation/#news-sentiment](https://www.alphavantage.co/documentation/#news-sentiment)
3. **Polygon**:
    - API này giúp truy xuất dữ liệu OHLC (giá mở cửa, cao nhất, thấp nhất và đóng cửa) hàng ngày của tất cả cổ phiếu trên thị trường chứng khoán Mỹ.
    - Thông tin chi tiết: [polygon.io/docs/stocks/get_v2_aggs_ticker__stocksticker__range__multiplier___timespan___from___to](https://polygon.io/docs/stocks/get_v2_aggs_ticker__stocksticker__range__multiplier___timespan___from___to)

## B. Dữ liệu trả về từ API

### 1. sec-api.io

- **name**: Tên công ty.
- **ticker**: Ký hiệu trên sàn giao dịch chứng khoán.
- **cik**: Mã CIK.
- **cusip**: Số CUSIP.
- **exchange**: Sàn giao dịch.
- **isDelisted**: Giá trị boolean cho biết liệu cổ phiếu đã bị loại khỏi sàn.
- **category**: Hạng mục cổ phiếu.
- **sector**: Ngành của công ty.
- **industry**: Ngành cụ thể của công ty.
- **sic**: Mã SIC.
- **sicSector**: Ngành dựa trên mã SIC.
- **sicIndustry**: Ngành cụ thể dựa trên mã SIC.
- **famaSector**: Ngành theo mô hình Fama-French.
- **famaIndustry**: Ngành theo mô hình Fama-French.
- **currency**: Đơn vị tiền tệ giao dịch.
- **location**: Địa điểm trụ sở công ty.
- **id**: Định danh công ty.

### 2. Alpha Vantage API for market status

- **market_type**: Loại thị trường.
- **region**: Khu vực thị trường.
- **primary_exchanges**: Sàn giao dịch chính.
- **local_open**: Thời gian mở cửa địa phương.
- **local_close**: Thời gian đóng cửa địa phương.
- **current_status**: Tình trạng hiện tại của thị trường.

### 3. Alpha Vantage API for news sentiment

- **title**: Tiêu đề bài viết.
- **url**: Đường dẫn bài viết.
- **time_published**: Thời gian xuất bản.
- **authors**: Tác giả.
- **summary**: Tóm tắt bài viết.
- **source**: Nguồn tin.
- **source_domain**: Tên miền của nguồn tin.
- **topics**: Danh sách chủ đề liên quan.
- **relevance_score**: Điểm độ liên quan của bài viết.
- **overall_sentiment_score**: Điểm cảm xúc tổng thể.
- **overall_sentiment_label**: Nhãn cảm xúc tổng thể.
- **ticker_sentiment**: Cảm xúc của cổ phiếu.
- **ticker**: Mã cổ phiếu.
- **ticker_sentiment_score**: Điểm cảm xúc của cổ phiếu.
- **ticker_sentiment_label**: Nhãn cảm xúc của cổ phiếu.

Chỉ số cảm xúc (sentiment_score_definition):

- **Bearish**: x <= -0.35
- **Somewhat-Bearish**: -0.35 < x <= -0.15
- **Neutral**: -0.15 < x < 0.15
- **Somewhat-Bullish**: 0.15 <= x < 0.35
- **Bullish**: x >= 0.35

Chỉ số liên quan (relevance_score_definition): 0 < x <= 1, điểm số càng cao thì độ liên quan càng cao.

### 4. Polygon

- **T**: Mã cổ phiếu.
- **o**: Giá mở cửa.
- **h**: Giá cao nhất.
- **l**: Giá thấp nhất.
- **c**: Giá đóng cửa.
- **v**: Khối lượng giao dịch.
- **vw**: Giá trung bình theo khối lượng
- **n**: số lượng giao dịch
- **t**: thời gian ngày giao dịch

## C. Thời gian query API

- **sec-api.io**: 0h ngày đầu tiên của mỗi tháng.
- **Alpha Vantage API for market status**: 0h ngày đầu tiên của mỗi tháng.
- **Alpha Vantage API for news sentiment**:
    - Các khung giờ giao dịch trong ngày
        - 0h - 9h30
        - 9h30 - 16h
        - 16h - 0h
- **Polygon**: 1h đầu ngày.

## D. Phạm vi dữ liệu

- Sàn giao dịch chứng khoán Mỹ (NYSE, NASDAQ).
- Dữ liệu OHLC từ ngày 11-06-2024 đến hiện tại.
- Tin tức và bài viết từ ngày 11-06-2024 đến hiện tại.
- Các chủ đề liên quan đến thị trường chứng khoán.

## E. Khối lượng dữ liệu cần xử lý

- **OHLC**: Khoảng 10,000 dòng dữ liệu mỗi ngày.
- **Bài viết**: Khoảng 500 bài viết mỗi ngày.
- **Dữ liệu công ty**: Khoảng 28,000 dòng được cập nhật mỗi tháng.

## F. Thiết kế Database

- Ta có thể thấy 2 API **sec-api.io** và **Alpha Vantage API for market status** không cần phải query thường xuyên như 2 API còn lại vì dữ liệu trong 2 API này hiếm khi thay đổi và chỉ cần cập nhật vào đầu tháng.
- Do đó, ta sẽ lưu dữ liệu từ 2 API này vào Database nhằm giả lập Backend Database làm Data Source thêm đa dạng.
- Database được chuẩn hóa 3NF gồm 5 table sau:
    
    ![Untitled](Chu%CC%9Bo%CC%9Bng%201%20DESIGN%20b5fd773ef08a4b1b8e39a3c13c5e6927/Untitled.png)
    

## **G. Xác định các bài toán được đặt ra**

Từ dữ liệu thu được đặt ra các bài toán cần xử lý từ đó xác định và thiết kế Data Warehouse

- **Business Requirement #1**: Phân tích xu hướng giá cổ phiếu
    - Theo dõi chỉ số OHLC của từng cổ phiếu sau mỗi ngày giao dịch.
    - Theo dõi xu hướng giá của từng cổ phiếu theo các mốc thời gian khác nhau (ngày, tuần, tháng, quý, năm).
    - Xác định các cổ phiếu có xu hướng tăng, giảm hoặc đi ngang trong một khoảng thời gian nhất định.
    - Dự đoán xu hướng giá tương lai của các cổ phiếu dựa trên dữ liệu lịch sử và các chỉ số phân tích khác.
- **Business Requirement #2**: Phân tích thị trường
    - Theo dõi cảm xúc chung của thị trường (bullish, bearish, neutral) dựa trên các nguồn dữ liệu khác nhau (mạng xã hội, tin tức, diễn đàn tài chính).
    - Xác định các chủ đề ảnh hưởng đến tâm lý thị trường (sự kiện kinh tế, chính trị, v.v.).
    - Phân tích sentiment của các chủ đề tin tức (tích cực, tiêu cực, trung lập).
    - Phân tích tác động của các chủ đề tin tức đến giá cổ phiếu.
- **Business Requirement #3**: Phân tích khối lượng giao dịch
    - Theo dõi khối lượng giao dịch của từng cổ phiếu theo ngày, tuần, tháng.
    - Xác định các cổ phiếu có khối lượng giao dịch cao bất thường.
    - Phân tích mối quan hệ giữa khối lượng giao dịch và giá cổ phiếu.
- **Business Requirement #4**: Phân tích các nhóm ngành
    - Xác định và phân tích các nhóm ngành trên thị trường chứng khoán.
    - Đánh giá hiệu quả hoạt động của từng nhóm ngành.
    - Xác định các nhóm ngành tiềm năng đầu tư

## H. Thiết kế hệ thống ELT

### **1. Galaxy Schema**:

- Thiết kế bảng Dimension và bảng Fact cho các Business Requirement từ Data Source là 2 API và 1 Database ta có được cấu trúc của Data Warehouse như sau:
    
    ![Untitled](Chu%CC%9Bo%CC%9Bng%201%20DESIGN%20b5fd773ef08a4b1b8e39a3c13c5e6927/Untitled%201.png)
    

### **2. ELT Diagram & Taskflow**:

- Lưu đồ công việc của quá trình ELT.
    
    ![Untitled](Chu%CC%9Bo%CC%9Bng%201%20DESIGN%20b5fd773ef08a4b1b8e39a3c13c5e6927/Untitled%202.png)
    
    ![Untitled](Chu%CC%9Bo%CC%9Bng%201%20DESIGN%20b5fd773ef08a4b1b8e39a3c13c5e6927/Untitled%203.png)
    

### **3. ELT Tools**:

- Các công cụ sử dụng cho quá trình ELT.
    
    ![Untitled](Chu%CC%9Bo%CC%9Bng%201%20DESIGN%20b5fd773ef08a4b1b8e39a3c13c5e6927/Untitled%204.png)
    

### **4. ELT BPMN**:

- Mô hình quy trình cho ELT.
    
    ![Untitled](Chu%CC%9Bo%CC%9Bng%201%20DESIGN%20b5fd773ef08a4b1b8e39a3c13c5e6927/Untitled%205.png)
    

### **5. File System**:

- Hệ thống tệp lưu trữ dữ liệu.
- ETL cho Database Backend
    
    ![Untitled](Chu%CC%9Bo%CC%9Bng%201%20DESIGN%20b5fd773ef08a4b1b8e39a3c13c5e6927/Untitled%206.png)
    
- ELT cho Data Warehouse
    
    ![Untitled](Chu%CC%9Bo%CC%9Bng%201%20DESIGN%20b5fd773ef08a4b1b8e39a3c13c5e6927/Untitled%207.png)
    
- Cấu hình DB và DW
    
    ![Untitled](Chu%CC%9Bo%CC%9Bng%201%20DESIGN%20b5fd773ef08a4b1b8e39a3c13c5e6927/Untitled%208.png)
    
- Cấu hình Dag
    
    ![Untitled](Chu%CC%9Bo%CC%9Bng%201%20DESIGN%20b5fd773ef08a4b1b8e39a3c13c5e6927/Untitled%209.png)
    

### **6. Thiết kế DAGs**:

- Thiết kế các DAGs để quản lý luồng dữ liệu.

![Untitled](Chu%CC%9Bo%CC%9Bng%201%20DESIGN%20b5fd773ef08a4b1b8e39a3c13c5e6927/Untitled%2010.png)

![Untitled](Chu%CC%9Bo%CC%9Bng%201%20DESIGN%20b5fd773ef08a4b1b8e39a3c13c5e6927/Untitled%2011.png)

### **7. Data Flow Diagram**:

- Sơ đồ luồng dữ liệu trong hệ thống.

![Untitled](Chu%CC%9Bo%CC%9Bng%201%20DESIGN%20b5fd773ef08a4b1b8e39a3c13c5e6927/Untitled%2012.png)

![Untitled](Chu%CC%9Bo%CC%9Bng%201%20DESIGN%20b5fd773ef08a4b1b8e39a3c13c5e6927/Untitled%2013.png)