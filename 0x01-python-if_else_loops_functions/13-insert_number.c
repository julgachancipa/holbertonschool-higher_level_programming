#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list..
 * @head: header node
 * @number: node's new number
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *follow, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	prev = *head;
	follow = prev->next;
	while (prev)
	{
		if (prev->n >= number)
		{
			new->next = prev;
			*head = new;
			return (new);
		}
		else if (!follow && prev->n <= number)
		{
			prev->next = new;
			new->next = NULL;
			return (new);
		}
		else if (prev->n <= number && follow->n >= number)
		{
			prev->next = new;
			new->next = follow;
			return (new);
		}
		prev = follow;
		follow = prev->next;
	}
	return (NULL);
}
