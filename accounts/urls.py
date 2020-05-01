from django.urls import path, include
from django.contrib import admin
from PUGCGRADEBOOK import settings
from . import views, AdminViews


urlpatterns = [
      #  path('dashboard/',views.home),
        path('',views.ShowLoginPage),
        path('doLogin',views.doLogin, name="do_login"),
        path('get_user_details',views.GetUserDetials, name="get_user_detail"),
        path('logout_user',views.logout_user, name="logout_user"),
        path('admin_home',AdminViews.admin_home, name="admin_home"),
        path('add_staff',AdminViews.add_staff, name="add_staff"),
        path('add_staff_save',AdminViews.add_staff_save, name="add_staff_save"),
        path('add_department',AdminViews.add_department, name="add_department"),
        path('add_department_save',AdminViews.add_department_save, name="add_department_save"),
        path('add_program',AdminViews.add_program, name="add_program"),
        path('add_program_save',AdminViews.add_program_save, name="add_program_save"),
        path('add_student',AdminViews.add_student, name="add_student"),
        path('add_student_save',AdminViews.add_student_save, name="add_student_save"),
        path('add_subject',AdminViews.add_subject, name="add_subject"),
        path('add_subject_save',AdminViews.add_subject_save, name="add_subject_save"),
        path('manage_staff',AdminViews.manage_staff, name="manage_staff"),
        path('manage_student',AdminViews.manage_student, name="manage_student"),
        path('manage_department',AdminViews.manage_department, name="manage_department"),
        path('manage_program',AdminViews.manage_program, name="manage_program"),
        path('manage_subject',AdminViews.manage_subject, name="manage_subject"),
        path('edit_staff/<str:staff_id>',AdminViews.edit_staff, name="edit_staff"),
        path('edit_staff_save', AdminViews.edit_staff_save, name="edit_staff_save"),
        path('edit_student/<str:student_id>',AdminViews.edit_student, name="edit_student"),
        path('edit_student_save', AdminViews.edit_student_save, name="edit_student_save"),
        path('edit_subject/<str:subject_id>',AdminViews.edit_subject, name="edit_subject"),
        path('edit_subject_save', AdminViews.edit_subject_save, name="edit_subject_save"),
        path('edit_department/<str:department_id>', AdminViews.edit_department, name="edit_department"),
        path('edit_department_save', AdminViews.edit_department_save, name="edit_department_save"),
        path('edit_program/<str:course_id>', AdminViews.edit_program, name="edit_program"),
        path('edit_program_save', AdminViews.edit_program_save, name="edit_program_save"),
]
