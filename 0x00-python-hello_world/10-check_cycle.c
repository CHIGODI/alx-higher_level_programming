#include "lists.h"
/**
 * check_cycle - checks if a linked list has a cycle
 * @list: list
 *
 * Return: 1 if list has cycle 0 otherwise
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = fast = list;

	while (list != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;

		if (fast == slow)
			return (1);
	}
	return (0);
}
