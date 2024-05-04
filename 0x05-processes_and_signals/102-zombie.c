#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - Infinite loop
 * Return: Always 0.
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
/**
 * main - Entry point
 *
 * Return: Always 0.
 */
int main(void)
{
    int i;
    pid_t zombie_pid;

    for (i = 0; i < 5; i++)
    {
        zombie_pid = fork();
        if (zombie_pid == 0)
            exit(0);
        else
            printf("Zombie process created, PID: %d\n", zombie_pid);
    }

    infinite_while();
    return (0);
}
