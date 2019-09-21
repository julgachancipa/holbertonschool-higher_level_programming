#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * listint_len - return num of the elements.
 * @h: head pointer.
 * Return: # of elements.
 */
size_t listint_len(const listint_t *h)
{
	size_t nodes = 0;

	while (h != NULL)
	{
		h = h->next;
		nodes++;
	}
	return (nodes);
}
/**
 * get_n_at_index - returns the nth node
 * of a listint_t linked list.
 * @head: head pointer.
 * @index: position of the node that will be returned.
 * Return: nth n
 */
int get_n_at_index(listint_t *head, unsigned int index)
{
	unsigned int i = 0;
	listint_t *current = head;

	while (current != NULL)
	{
		if (i == index)
		{
			break;
		}
		current = current->next;
		i++;
	}
	return (current->n);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: header node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	size_t len, i;
	int a, b;

	if (*head == NULL)
		return (1);
	len = listint_len(*head);
	for (i = 0; i < len / 2; i++)
	{
		a = get_n_at_index(*head, i);
		b = get_n_at_index(*head, len - i - 1);
		if (a != b)
			return (0);
	}
	return (1);
}
