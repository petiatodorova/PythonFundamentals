class Website:
    def __init__(self, host, domain, queries):
        self.host = host
        self.domain = domain
        self.queries = self.set_queries_list(queries)

    def set_queries_list(self, queries):
        temp_list = []
        temp_list.extend(queries)
        return temp_list


websites_list = []

line_stream = input().split(" | ")

while not line_stream[0] == "end":
    cur_host = line_stream[0]
    cur_domain = line_stream[1]
    if len(line_stream) > 2:
        cur_queries = line_stream[2].split(",")
    else:
        cur_queries = ""

    # feed
    current_website = Website(cur_host, cur_domain, cur_queries)
    websites_list.append(current_website)
    line_stream = input().split(" | ")

# print
for web in websites_list:
    if not web.queries == []:
        queries_str = "]&[".join(web.queries)
        print(f"https://www.{web.host}.{web.domain}/query?=[{queries_str}]")

    else:
        print(f"https://www.{web.host}.{web.domain}")
