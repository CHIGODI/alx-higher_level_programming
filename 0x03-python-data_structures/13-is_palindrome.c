#include "lists.h"
/**
 * reverse - function to reverse a singly linked list
 * @head: pointer to pointer to first  node
 *
 * Return: pointer to first node
 *
 */
listint_t *reverse(listint_t **head)
{
	listint_t *prev, *curr, *temp;

	temp = *head;
	prev = curr = NULL;

	while (temp != NULL)
	{
		curr = temp;
		temp = temp->next;
		curr->next = prev;
		prev = curr;
	}
	*head = curr;
	return (*head);
}
/**
 * is_palindrome - function that checks if a singly linked
 *                 list is a palidnrome
 * @head: pointer to first node
 *
 * Return: 0 if is not 1 otherwise
 *
 */
int is_palindrome(listint_t **head)
{
	listint_t *rev_list, *temp;

	if (*head == NULL)
		return (0);

	rev_list = reverse(head);
	temp = *head;

	while (temp != NULL && rev_list != NULL)
	{
		if (temp->n != rev_list->n)
		{
			return (0);
		}
		else
		{
			return (1);
		}
	}
}
