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

	if (list == NULL)
		return (0);

	slow = list;
	fast = list->next;

	while(list != NULL && fast->next)
	{
		if (fast == slow)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
