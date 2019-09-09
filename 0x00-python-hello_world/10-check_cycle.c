#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle -  checks if a singly linked list has a cycle in it.
 * @list: |||
 * Return: 0 no cycle or 1 if it is
 */
int check_cycle(listint_t *list)
{
	listint_t *head;

	head = malloc(sizeof(int *));
	if (!head)
		exit(EXIT_FAILURE);
	head = list;
	while (list->next != NULL)
	{
		if (list->next == head)
			return (1);
		list = list->next;
	}
	return (0);
}
