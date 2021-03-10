import psutil
def get_netcard():
    """获取网卡名称和ip地址
    """
    netcard_info = []
    info = psutil.net_if_addrs()
    print(info.items())
    for k, v in info.items():
        for item in v:
            if item[0] == 2 and not item[1] == '127.0.0.1' :
                #去除通过dhcp获取ip方式没获取时分配的的自动专有地址
                if "169.254."not in item[1]:
                    # netcard_info.append((k, item[1]))
                    netcard_info.append(item[1])
        print("K",k)
        #test
    return netcard_info
if __name__ == '__main__':
    print(get_netcard())


