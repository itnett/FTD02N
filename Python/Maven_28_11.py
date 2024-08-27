python
    from graphviz import Digraph

    def generate_uml():
        dot = Digraph(comment='Employee Management System')

        dot.node('E', 'Employee')
        dot.node('M', 'Manager')
        dot.node('D', 'Department')

        dot.edges(['ED', 'MD'])
        dot.edge('D', 'M', constraint='false')

        dot.render('uml_diagram.gv', view=True)

    generate_uml()