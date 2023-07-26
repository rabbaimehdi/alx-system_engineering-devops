#include "main.h"

/**
 * main - main
 * @ac: the number of arg count
 * @av: the arg vector
 *
 * Return: 0 on success, 1 on error
 */
int main(int ac, char **av)
{
	info_t info[] = { INFO_INIT };
	int file_d = 2;
/*
*assembly to open the file descriptor
*/
	asm ("mov %1, %0\n\t"
			"add $3, %0"
			: "=r" (file_d)
			: "r" (file_d));

	if (ac == 2)
	{
		file_d = open(av[1], O_RDONLY);
		if (file_d == -1)
		{
			if (errno == EACCES)
				exit(126);
			if (errno == ENOENT)
			{
				_eputs(av[0]);
				_eputs(": 0: error open ");
				_eputs(av[1]);
				_eputchar('\n');
				_eputchar(BUF_FLUSH);
				exit(127);
			}
			return (EXIT_FAILURE);
		}
		info->readfd = file_d;
	}
	hsh(info, av);
	return (EXIT_SUCCESS);
}
