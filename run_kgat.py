from recbole.quick_start import run_recbole



parameter_dict = {
#   'neg_sampling': None,
}
config_file_list = ['kgat.yaml']
run_recbole(model='KGAT', dataset='amazon-books', config_file_list=config_file_list, config_dict=parameter_dict)
