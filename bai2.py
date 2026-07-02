# code đã sửa
from fastapi import FastAPI , HTTPException
app = FastAPI()
orders = [
    {"id": 1, "customer_name": "Nguyễn Văn An", "total": 250000, "status": "pending"},
    {"id": 2, "customer_name": "Trần Thị Bình", "total": 500000, "status": "paid"},
    {"id": 3, "customer_name": "Lê Văn Cường", "total": 150000, "status": "cancelled"},
    {"id": 4, "customer_name": "Phạm Thị Dung", "total": 320000, "status": "pending"}
]
@app.get("/orders/status/{status}")
def get_orders_by_status(status: str):
    result = []

    for order in orders:
        if order['status'] == status:
            result.append(order)
        
    if len(result) == 0 :
        raise HTTPException (
            status_code=400,
            detail="Trạng thái đơn hàng không hợp lệ"
        )
    
    return result

# Endpoint hiện tại có Path Parameter là {status}
# Path Parameter trong bài này là status
# Khi gọi /orders/status/pending, biến status nhận giá trị status = "pending"
# API hiện tại trả về sai dữ liệu vì ghi return orders khiến nó trả về danh sách tất cả đơn hàng
# Dòng code khiến API bỏ qua giá trị của status là return orders