#include "lists.h"

/**
 * check_cycle - function to check if there is a looop in list
 * @list: list to check through
 * Return: 0 if not, otherwise 1
 */

int check_cycle(listint_t *list)
{
	listint_t *p, *q;

	if (list != NULL)
	{
		p = q = list;
		while (p && q)
		{
			p = p->next;
			q = q->next->next;
			if (p == q)
				return (1);
		}
	}
	return (0);
}
