import duckdb

# Kết nối đến DuckDB (hoặc tạo cơ sở dữ liệu mới nếu chưa tồn tại)
conn = duckdb.connect('/home/anhcu/Final_ETL_App/etl-app/datawarehouse.duckdb')

# # Xóa bảng fact_candles nếu nó tồn tại
# conn.execute('DROP TABLE IF EXISTS fact_candles CASCADE;')

# Tạo bảng fact_candles mới
create_table_query = """
CREATE TABLE IF NOT EXISTS fact_candles (
    candle_id INTEGER DEFAULT NEXTVAL('candle_id_seq') PRIMARY KEY,
    candle_company_id INTEGER NOT NULL,
    candle_volume INTEGER NOT NULL,
    candle_volume_weighted DOUBLE NOT NULL,
    candle_open DOUBLE NOT NULL,
    candle_close DOUBLE NOT NULL,
    candle_high DOUBLE NOT NULL,
    candle_low DOUBLE NOT NULL,
    candle_time_stamp CHAR(15) NOT NULL,
    candle_num_of_trades INTEGER NOT NULL,
    candle_is_otc BOOLEAN DEFAULT false,
    candles_time_id INTEGER,
    FOREIGN KEY (candle_company_id) REFERENCES dim_companies(company_id),
    FOREIGN KEY (candles_time_id) REFERENCES dim_time(time_id)
);
"""

conn.execute(create_table_query)

# Đóng kết nối
conn.close()
