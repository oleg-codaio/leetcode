/**
 * Given an absolute path for a file (Unix-style), simplify it.
 *
 * @lc_runtime 0 ms
 * @author oleg@osv.im
 */

#include <string.h>
#include <stdbool.h>
#include <stdio.h>

char* simplifyPath(char* path) {
    int finalStrLen = 1;
    
    if (!path || path[0] != '/') {
        return NULL;
    }

    int i = 1;
    bool newWord = true;
    bool specialCase = false;
    char curr;

    // Zero out all canceled values.
    while (true) {
        curr = path[i];

        if (curr == '\0') {
            break;
        } else if (curr == '/') {
            if (path[finalStrLen - 1] == '/') {
                // / - White out and skip this space.
                path[i] = '\0';
                i++;
            } else {
                // New word started.
                newWord = true;
                i++;
            }
        } else {
            specialCase = false;

            if (newWord && curr == '.') {
                if (path[i + 1] == '/' || path[i + 1] == '\0') {
                    // ./ - ignore.
                    if (path[i + 1] == '\0') {
                        break;
                    } else {
                        i += 2;
                        specialCase = true;
                    }
                } else if (path[i + 1] == '.' && (path[i + 2] == '/' || path[i + 2] == '\0')) {
                    // ../ - erase backwards.
                    while (finalStrLen > 1 && path[finalStrLen - 1] != '/') {
                        path[finalStrLen - 1] = '\0';
                        finalStrLen--;
                    }

                    // Delete trailing '/' if we can (smallest string: '/a/')
                    if (finalStrLen >= 3) {
                        path[finalStrLen - 1] = '\0';
                        finalStrLen--;
                    }

                    if (path[i + 2] == '\0') {
                        break;
                    } else {
                        i += 3;
                        specialCase = true;
                    }
                }
            }

            if (!specialCase) {
                if (newWord) {
                    newWord = false;
                    if (finalStrLen > 1) {
                        path[finalStrLen] = '/';
                        finalStrLen++;
                    }
                }
                path[finalStrLen] = curr;
                finalStrLen++;
                i++;
            }
        }
    }
    
    // End the string early.
    path[finalStrLen] = '\0';
    
    return path;
}

int main(int argc, char* argv[]) {
    if (argc == 2) {
        printf("%s\n", simplifyPath(argv[1]));
        return 0;
    } else {
        return 1;
    }
}
