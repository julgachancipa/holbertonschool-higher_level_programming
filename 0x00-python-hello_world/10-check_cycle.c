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
	listint_t *past, *future;

	past = list;
	future = list->next;
	while (future)
	{
		if (past == future)
		{
			return (1);
		}
		past = past->next;
		future = future->next;
		if (!future)
			break;
		future = future->next;
	}
	return (0);
}
