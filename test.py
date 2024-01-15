from main import main

times = 100#试100轮
setup = []
commit = []
openVerify = []
recursive_protocol = []
PIOPprotocol = []
Decision = []
commonparameterssize = []
provesize = []
for i in range(1,times+1):
    print(f"--------------------当前进行第 {i}轮测试--------------------".center(50))
    setup_time, commit_time, openVerify_time, recursive_protocol_time, PIOPprotocol_time, Decision_time, judge, common_parameters_size, prove_size = main()
    setup.append(setup_time)
    commit.append(commit_time)
    openVerify.append(openVerify_time)
    recursive_protocol.append(recursive_protocol_time)
    PIOPprotocol.append(PIOPprotocol_time)
    Decision.append(Decision_time)
    commonparameterssize.append(common_parameters_size)
    provesize.append(prove_size)
ave_setup = sum(i for i in setup) / times
ave_commit = sum(i for i in commit) / times
ave_openVerify = sum(i for i in openVerify) / times
ave_recursive_protocol = sum(i for i in recursive_protocol) / times
ave_PIOPprotocol = sum(i for i in PIOPprotocol) / times
ave_Decision = sum(i for i in Decision) / times
ave_commonp_size = sum(i for i in commonparameterssize) / times
ave_prove_size = sum(i for i in provesize) / times
print(f"测试 {times}次")
print("时间开销统计：")
print(f"setup平均时间开销为 {round(ave_setup + ave_commit + ave_openVerify,5)}")
print(f"PIOPprotocol平均时间开销为 {round(ave_recursive_protocol + ave_PIOPprotocol,5)}")
print(f"Decision平均时间开销为 {round(ave_Decision,5)}")
print("公共参数及证明：")
print(f"size of common parameters : {round(ave_commonp_size,5)}")
print(f"size of prove : {round(ave_prove_size,5)}")
