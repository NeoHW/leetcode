# Task Scheduling Problem

Given an array `task_memory` of `n` positive integers representing the amount of memory required to process each task, an array `task_type` of `n` positive integers representing the type of each task, and an integer `max_memory`, find the minimum amount of time required for the server to process all the tasks.

Each task takes 1 unit of time to process. The server can process at most two tasks in parallel only if they are of the same type and together require no more than `max_memory` units of memory.

## Example

Suppose `n = 4`, `task_memory = [7,2,3,9]`, `task_type = [1,2,1,3]`, and `max_memory = 10`.

One efficient schedule is shown:

| Task Pair | Task 1 | Task 2 | Task Type | Memory requirements | Within Max Memory | Parallel? |
|-----------|--------|--------|-----------|---------------------|-------------------|-----------|
| 1         | 0      | 2      | Same      | 7 + 3 = 10          | Yes               | Yes       |
| 2         | 1      | 3      | Different | 9 + 2 = 11          | No                | No        |

Task 0 and 2 are processed concurrently, but the other two must be processed separately due to their memory requirements and because they are not the same type. The minimum amount of time required to process all the tasks is 3 units.