import matplotlib.pyplot as plt

def printMat(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print("{:^6s}".format(str(m[i][j])), end='|')
        print()

class Vertices(object):
    def __init__(self,name="",degree=0,data=object):
        self.name=name
        self.degree=degree
        self.data=data

    def __cmp__(self, other):
        if not isinstance(other,Vertices) or\
                self.data != other.data:
            return False
        return True
    def __str__(self):
        return "{}:{}".format(self.name,self.data)

class Edge(object):
    def __init__(self,fromVertices,toVertices,directed=False, weight=1):
        self.fromV=fromVertices
        self.toV=toVertices
        self.dircted=directed
        self.weight=weight

    def __cmp__(self, other):
        if not isinstance(other,Edge) or \
            self.fromV != other.fromV or \
            self.toV != other.toV or \
            self.directed != other.directed or \
                self.weight != other.weight:
            return False
        return True

    def __str__(self):
        return "->{}->{}".format(self.weight,self.toV)


class Graph(object):

    def __init__(self,G=dict(),graphid="",directed=False):
        self.graph=G
        self.directed=directed
        self.id=graphid


    def addEdge(self,fromVertices, toVertices,weight=1):
        if fromVertices not in self.graph or \
                        toVertices not in self.graph:
            raise Exception("Vertices error not in the graph")
        else:
            e=Edge(fromVertices,toVertices,self.directed,weight)
            self.graph[fromVertices].append(e)
            if not self.directed:
                e=Edge(toVertices,fromVertices,self.directed,weight)
                self.graph[toVertices].append(e)

    def addVertices(self,vertices):
        if vertices not in self.graph:
            self.graph[vertices]=list()

    def createMatrix(self):
        self.matrix=[["inf" for x in range(len(self.graph))] for x in range(len(self.graph))]
        self.phi=[["NIL" for x in range(len(self.graph))] for x in range(len(self.graph))]
        for i in self.graph:
            x=int(i.name)
            self.matrix[x-1][x-1]=0
            self.phi[x-1][x-1]="NIL"
            for j in self.graph[i]:
                self.matrix[x-1][int(j.toV.name)-1]=j.weight
                self.phi[x-1][int(j.toV.name)-1]=x

    def dikstra(self,src=0):
        res=[None]*len(self.graph)
        maxHeap=[None]*len(self.graph)
        res[src]=0
        for i in self.graph[src]:
            pass



    def floydWarshall(self):
        self.createMatrix()
        src=[x[:] for x in self.matrix]
        dst=[x[:] for x in self.matrix]
        phiTmp=[x[:] for x in self.phi]
        n=len(self.graph)
        for k in  range(n):
            for i in range(n):
                for j in range(n):
                    try:
                        if src[i][j]=="inf" or\
                         src[i][j]>src[i][k]+src[k][j]:
                            if type(src[i][k]) is str or \
                                    type(src[k][j]) is str:
                                dst[i][j]="inf"
                            else:
                                dst[i][j]=int(src[i][k])+int(src[k][j])
                                phiTmp[i][j]=k+1
                        else:
                            dst[i][j]=int(src[i][j])
                    except:
                        pass
            src=[x[:] for x in dst]
            print("k={}".format(k))
            printMat(dst)
            print()
            printMat(phiTmp)
            print()
        return dst,phiTmp

    def __str__(self):
        res="Graph {}\n{}\n".format(self.id,"="*10)
        res="{} Adjacency list:\n".format(res)
        for i in self.graph:
            a=""
            for j in self.graph[i]:
                a= a+ " , " +str(j)
            res+="{}: {}\n".format(i,a)
        res+="\n"

        return res





def main():
    v1=Vertices("1",data="22")
    v2=Vertices("2",data="23")
    v3=Vertices("3",data="25")
    v4=Vertices("4",data="25")
    v5=Vertices("5",data="25")

    graph=Graph(graphid="Itzik Graph",directed=True)
    graph.addVertices(v1)
    graph.addVertices(v2)
    graph.addVertices(v3)
    graph.addVertices(v4)
    graph.addVertices(v5)


    graph.addEdge(v1,v2,3)
    graph.addEdge(v1,v3,8)
    graph.addEdge(v1,v5,-4)
    graph.addEdge(v2,v5,7)
    graph.addEdge(v2,v4,1)
    graph.addEdge(v3,v2,4)
    graph.addEdge(v4,v3,-5)
    graph.addEdge(v4,v1,2)
    graph.addEdge(v5,v4,6)
    print(graph)
    graph.createMatrix()
    printMat(graph.matrix)
    print()
    printMat (graph.phi)
    x,y =graph.floydWarshall()
    print()
    printMat(x)
    print()
    printMat(y)




if __name__ == '__main__':
    main()