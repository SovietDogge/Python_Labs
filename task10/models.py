from printing_funcions import print_models, show_completed_models

if __name__ == '__main__':
    unprinted_design = ['iphone_case', 'robot pendant', 'dodecahedron']
    completed_models = []
    print_models(unprinted_design, completed_models)
    show_completed_models(completed_models)
