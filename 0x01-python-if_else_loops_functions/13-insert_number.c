#include "lists.h"
#include "stdlib.h"
/**
 * insert_node - a function that inserts a number into a sorted singly
 *               linked list
 * @head: pointer to first node
 * @number: number to be inserted
 *
 * Return: address of new node
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *prev_node, *curr_node;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	curr_node = *head;
	while(curr_node != NULL)
	{
		if (curr_node->n >= number)
		{
			prev_node->next = new_node;
			new_node->n = number;
			new_node->next = curr_node;

			break;
		}
		prev_node = curr_node;
		curr_node = curr_node->next;
	}
	return (new_node);
}
