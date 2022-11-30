#include "lists.h"

/**
 * check_cycle - check if linked list has a cycle
 * @list: pointer to head node
 * Return: 1 if there is a cycle, 0 if there is'nt
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	while (first && second && first->next)
	{
		first = first->next->next;
		second = second->next;

		if (first == second)
			return (1);
	}

	return (0);
}
