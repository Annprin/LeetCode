class Solution:
    def simplifyPath(self, path: str) -> str:
        last = []
        path = path.split('/')
        for d in path:
            match d:
                case '':
                    pass
                case '.':
                    pass
                case '..':
                    if last:
                        last.pop()
                case default:
                    last.append(d)
        return '/' + '/'.join(last)