```markdown
student_management/
│
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── student.py
└── views/
    └── student_views.xml


└── static/description/
    └── icon.png
    └── banner.png 
```



Inside the Odoo web interface:


- Go to Apps (or Apps → Apps).

- In the search bar, remove the “Apps” filter (so all modules show).

- Click “Update Apps List” (or in newer versions: “Update Apps” under the debug menu).

Recordar que tenemos que actualizar el módulo para que se vea reflejados los cambios. Si no va, intentas con un:

```bash
$ docker compose restart odoo
```


```xml
<odoo>
    <!-- Views -->
    <record id="view_student_form" model="ir.ui.view">
        ...
    </record>

    <record id="view_student_list" model="ir.ui.view">
        ...
    </record>

    <!-- Action -->
    <record id="action_student_management" model="ir.actions.act_window">
        <field name="name">Students</field>
        <field name="res_model">student.management</field>
        <field name="view_mode">list,form</field>
    </record>

    <!-- Menus -->
    <menuitem id="menu_student_root" name="Student Management"/>
    <menuitem id="menu_student" name="Students" parent="menu_student_root" action="action_student_management"/>
</odoo>
```