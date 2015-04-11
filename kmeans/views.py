from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context = {
		'columns': [
			[0, 'duration'],
			[4, 'src_bytes'],
			[5, 'dst_bytes'],
			[7, 'wrong_fragment'],
			[8, 'urgent'],
			[9, 'hot'],
			[10, 'num_failed_logins'],
			[12, 'num_compromised'],
			[13, 'root_shell'],
			[14, 'su_attempted'],
			[15, 'num_root'],
			[16, 'num_file_creations'],
			[17, 'num_shells'],
			[18, 'num_access_files'],
			[19, 'num_outbound_cmds'],
			[22, 'count'],
			[23, 'srv_count'],
			[24, 'serror_rate'],
			[25, 'srv_serror_rate'],
			[26, 'rerror_rate'],
			[27, 'srv_rerror_rate'],
			[28, 'same_srv_rate'],
			[29, 'diff_srv_rate'],
			[30, 'srv_diff_host_rate'],
			[31, 'dst_host_count'],
			[32, 'dst_host_srv_count'],
			[33, 'dst_host_same_srv_rate'],
			[34, 'dst_host_diff_srv_rate'],
			[35, 'dst_host_same_src_port_rate'],
			[36, 'dst_host_srv_diff_host_rate'],
			[37, 'dst_host_serror_rate'],
			[38, 'dst_host_srv_serror_rate'],
			[39, 'dst_host_rerror_rate'],
			[40, 'dst_host_srv_rerror_rate'],
		]
	}
	return render(request, 'kmeans/index.html', context)

def scatterplot(request):
	columns = request.POST.getlist('columns[]')
	print(columns)
	return render(request, 'kmeans/index.html')