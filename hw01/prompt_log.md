# AI 辅助编程交互日志

## 1. 初始需求描述
**Prompt**:
"帮我用 Python 实现 n 皇后问题的求解器，要求：
1. 用回溯法，返回所有合法解，每个解用列表表示（索引为行，值为列，从 0 开始）
2. 提供 count_solutions 函数返回解的数量
3. 用 pytest 写单元测试，验证 N=4 有 2 个解，N=8 有 92 个解"

**AI 输出**:
生成了 `solve_eight_queens` 和 `count_solutions` 函数，以及基础测试用例 `test_n_queens_4` 和 `test_n_queens_8`。

---

## 2. 引入 Bug 并发现问题
### 2.1 手动引入 Bug
我修改了 `is_valid` 函数，**故意删除对角线检查**：
```python
def is_valid(row: int, col: int) -> bool:
    for r in range(row):
        c = board[r]
        if c == col:  # 遗漏了 `or abs(r - row) == abs(c - col)`
            return False
    return True