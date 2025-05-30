class Solution:
    def closestMeetingNode(self, edges, node1, node2):
        q = []
        q.append((node1,0,1)) # From node1 (node, distance, NumberToRecognizeWhichPath)
        q.append((node2,0,2))

        vis = {}
        result = -1
        minDist = sys.maxsize

        while q:
            node, dis, source = q.pop(0)
            if node in vis and source in vis[node]:
                continue

            if node in vis:
                vis[node][source] = dis
            else:
                vis[node]= {source:dis}

            # Check if both sources have reached this node
            if 1 in vis[node] and 2 in vis[node]:
                maxD = max(vis[node][1], vis[node][2])
                if maxD < minDist or (maxD == minDist and node < result):
                    result = node
                    minDist = maxD
                    # reason for not returning here directly in that 
                    # If multiple nodes have the same max distance, pick the smallest index. (asked in ques)
                    # return result

            nextNode = edges[node]
            if nextNode != -1:
                q.append((nextNode,dis+1,source))
        return result