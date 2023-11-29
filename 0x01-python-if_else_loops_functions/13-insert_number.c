#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to a pointer to the first node
 * @number: Number to be inserted
 *
 * Return: Address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *curr_node, *prev_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	curr_node = *head;
	prev_node = NULL;

	while (curr_node != NULL && curr_node->n < number)
	{
		prev_node = curr_node;
		curr_node = curr_node->next;
	}

	new_node->next = curr_node;

	if (prev_node == NULL)
		*head = new_node;
	else
		prev_node->next = new_node;

	return (new_node);
}
