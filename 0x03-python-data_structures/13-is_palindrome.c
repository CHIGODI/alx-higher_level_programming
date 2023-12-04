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
	listint_t *prev = NULL, *next = NULL, *current = NULL;

	current = *head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
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
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *temp, *rev;

	if (*head == NULL )
		return (1);

	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	rev = reverse(&slow->next);

	temp = *head;
	while(rev != NULL)
	{
		if (rev->n != temp->n)
		{
			return (0);
		}
		rev = rev->next;
		temp = temp->next;
	}
	return (1);
}
