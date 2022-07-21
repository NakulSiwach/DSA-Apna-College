# DAY 2  APNA COLLEGE SHEET


class Solution:

    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def diameter(self, root): # not calling height every time
        diameter = 0

        def height(root):
            nonlocal diameter
            if root is None:
                return 0
            lh = height(root.left)
            rh = height(root.right)
            diameter = max(diameter, 1 + lh + rh)
            return 1 + max(lh, rh)

        x = height(root)
        return diameter

    def reverseLevelOrder(root):
        if root is None:
            return []
        q = []
        l = [[root.data]]
        q.append(root)
        while len(q) > 0:
            temp = []
            z = len(q)
            for i in range(len(q)):
                if q[i].left is not None:
                    temp.append(q[i].left.data)
                    q.append(q[i].left)
                if q[i].right is not None:
                    temp.append(q[i].right.data)
                    q.append(q[i].right)
            for i in range(z):
                q.pop(0)
            if temp != []:
                l.append(temp)
        a = []
        for i in range(len(l) - 1, -1, -1):
            for j in range(len(l[i])):
                a.append(l[i][j])
        return a

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = []
        l = [[root.val]]
        q.append(root)
        while len(q) > 0:
            temp = []
            z = len(q)
            for i in range(len(q)):
                if q[i].left is not None:
                    temp.append(q[i].left.val)
                    q.append(q[i].left)
                if q[i].right is not None:
                    temp.append(q[i].right.val)
                    q.append(q[i].right)
            for i in range(z):
                q.pop(0)
            if temp != []:
                l.append(temp)
        return l

    def rightView(self, root):
        if root is None:
            return []
        q = []
        l = [[root.data]]
        q.append(root)
        while len(q) > 0:
            temp = []
            z = len(q)
            for i in range(len(q)):
                if q[i].left is not None:
                    temp.append(q[i].left.data)
                    q.append(q[i].left)
                if q[i].right is not None:
                    temp.append(q[i].right.data)
                    q.append(q[i].right)
            for i in range(z):
                q.pop(0)
            if temp != []:
                l.append(temp)
        a = []
        for i in range(len(l)):
            a.append(l[i][-1])
        return a

    def LeftView(root):
        if root is None:
            return []
        q = []
        l = [[root.data]]
        q.append(root)
        while len(q) > 0:
            temp = []
            z = len(q)
            for i in range(len(q)):
                if q[i].left is not None:
                    temp.append(q[i].left.data)
                    q.append(q[i].left)
                if q[i].right is not None:
                    temp.append(q[i].right.data)
                    q.append(q[i].right)
            for i in range(z):
                q.pop(0)
            if temp != []:
                l.append(temp)
        a = []
        for i in range(len(l)):
            a.append(l[i][0])
        return a

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if (p is None and q is not None) or (p is not None and q is None) or (p.val != q.val):
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)





