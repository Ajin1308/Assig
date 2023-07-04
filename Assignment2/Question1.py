class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_zero_sum_sublists(head):
    dummy = ListNode(0)
    dummy.next = head

    current = dummy
    running_sum = 0
    sum_map = {}

    while current:
        running_sum += current.val

        if running_sum == 0:
            dummy.next = current.next
            sum_map = {}
        elif running_sum in sum_map:
            prev = sum_map[running_sum].next
            temp_sum = running_sum + prev.val

            while prev != current:
                temp_sum += prev.val
                del sum_map[temp_sum]
                prev = prev.next

            sum_map[running_sum].next = current.next
        else:
            sum_map[running_sum] = current

        current = current.next

    return dummy.next
head = ListNode(3)
head.next = ListNode(4)
head.next.next = ListNode(-7)
head.next.next.next = ListNode(7)
head.next.next.next.next = ListNode(-1)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

new_head = delete_zero_sum_sublists(head)

current = new_head
while current:
    print(current.val, end=" ")
    current = current.next