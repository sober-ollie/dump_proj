char *ft_strchr(const char *s, int c)
{
    int i;
    char    *ptr;

    i = 0;
    ptr = (char *)s;
    while (ptr[i])
    {
        if ( c == ptr[i])
            return (&ptr[i]);
        i++;
    }
    if (ptr[i] == c)
        return (&ptr[i]);
    return (NULL);
}

int main()
{
    // printf("%s\n", ft_strchr("Hello", 'l'));
    // printf("%s\n", ft_strchr("Hello", 'o'));

    // printf("%s\n", ft_strchr("Hello", '\0'));
    char *result;

    result = ft_strchr("Hello", 'x');

    if (result != NULL)
        printf("%s\n", result);
    else
        printf("Character not found\n");
}


char *ft_strrchr(const char *s, int c)
{
    int l;

    l = 0;
    while (s[l])
    {
        l++;
    }
    while (l >= 0)
    {
        if (c == s[l])
            return ((char *)&s[l]);
        l--;
    }

    return (NULL);
}

int ft_strncmp(const char *s1, const char *s2, size_t n)
{
    size_t  i;
    
    i = 0;
    while ((s1[i] || s2[i]) && i < n)
    {
        if (s1[i] != s2[i])
            return (s1[i] - s2[i]);
        i++;
    }
    return (0);
}

void *ft_memchr(const void *s, int c, size_t n)
{

    unsigned char *ps;
    size_t  i;

    ps =  (unsigned char *)s;
    i = 0;
    while (i < n)
    {
        if (ps[i] == c)
            return (&ps[i]);
        i++;
    }
    return (NULL);
}

int ft_memcmp(const void *s1, const void *s2, size_t n)
{
    unsigned char *ps1;
    unsigned char *ps2;
    size_t  i;

    ps1 = (unsigned char *)s1;
    ps2 = (unsigned char *)s2;
    i = 0;

    while (i < n)
    {
        if (ps1[i] != ps2[i])
            return (ps1[i] - ps2[i]);
        i++;
    }
    return (0);
}


char *ft_strnstr(const char *big, const char *little, size_t len)
{
    size_t  i;
    size_t  j;

    i =  0;
    if (little[0] == '\0')
        return ((char *)&big[0]);
    while (big[i] && i < len)
    {
        j = 0;
        while((i + j) < len && big[i + j] == little[j] )
            j++;
        if (little[j] == '\0')
            return ((char *)&big[i]);
        i++;
    }
    return (NULL);

}

int sign_skip(const char *nptr, int *i)
{

    while (nptr[*i] == ' ' || (nptr[*i] >= 9  && nptr[*i] <= 13))
        (*i)++;
    if (nptr[*i] == '+' || nptr[*i] == '-')
    {
        if (nptr[*i] == '-')
        {
            (*i)++;
             return (-1);
        }
        (*i)++;
        return (1);
    }
    return (1);
}

int ft_atoi(const char *nptr)
{
    int i;
    int sign;
    int result;

    i = 0;
    sign = sign_skip(nptr, &i);
    result = 0;
    while (nptr[i] >= '0' && nptr[i] <= '9')
    {
        result = (result * 10) + (nptr[i] - '0');
        i++;
    }
    return (result * sign);
}
