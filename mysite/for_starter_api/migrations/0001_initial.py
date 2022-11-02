# Generated by Django 4.0.3 on 2022-10-27 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Businessschedule',
            fields=[
                ('businessschedule_number', models.AutoField(db_column='businessSchedule_number', primary_key=True, serialize=False)),
                ('businessschedule_title', models.CharField(db_column='businessSchedule_title', max_length=20)),
                ('businessschedule_content', models.TextField(db_column='businessSchedule_content')),
                ('businessschedule_plandate', models.DateTimeField(db_column='businessSchedule_planDate')),
                ('businessschedule_regidate', models.DateTimeField(db_column='businessSchedule_regiDate')),
                ('businessschedule_updatedate', models.DateTimeField(db_column='businessSchedule_updateDate')),
                ('information_creation_date', models.DateTimeField(blank=True, null=True)),
                ('information_revision_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'businessSchedule',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Counseling',
            fields=[
                ('counseling_number', models.AutoField(primary_key=True, serialize=False)),
                ('counseling_title', models.CharField(max_length=20)),
                ('counseling_content', models.TextField()),
                ('counseling_processing_phase', models.CharField(max_length=10)),
                ('counseling_processing_content', models.CharField(max_length=10)),
                ('counseling_note', models.CharField(max_length=255)),
                ('counseling_processing_date', models.DateTimeField()),
                ('information_creation_date', models.DateTimeField(blank=True, null=True)),
                ('information_revision_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'counseling',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CounselingManual',
            fields=[
                ('counseling_manual_number', models.AutoField(primary_key=True, serialize=False)),
                ('counseling_manual_title', models.CharField(max_length=30)),
                ('counseling_manual_content', models.CharField(blank=True, max_length=1024, null=True)),
                ('counseling_manual_creation_date', models.DateTimeField(blank=True, null=True)),
                ('counseling_manual_revision_date', models.DateTimeField(blank=True, null=True)),
                ('information_creation_date', models.DateTimeField(blank=True, null=True)),
                ('information_revision_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'counseling_manual',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CounselingManualComment',
            fields=[
                ('counseling_manual_comment_number', models.AutoField(primary_key=True, serialize=False)),
                ('counseling_manual_comment_content', models.CharField(blank=True, max_length=1024, null=True)),
                ('counseling_manual_comment_creation_date', models.DateTimeField(blank=True, null=True)),
                ('counseling_manual_comment_revision_date', models.DateTimeField(blank=True, null=True)),
                ('information_creation_date', models.DateTimeField(blank=True, null=True)),
                ('information_revision_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'counseling_manual_comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Counselingtype',
            fields=[
                ('counselingtype_number', models.AutoField(db_column='counselingType_number', primary_key=True, serialize=False)),
                ('counselingtype_largecategory', models.CharField(db_column='counselingType_largeCategory', max_length=10)),
                ('counselingtype_smallcategory', models.CharField(db_column='counselingType_smallCategory', max_length=10)),
                ('information_creation_date', models.DateTimeField(blank=True, null=True)),
                ('information_revision_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'counselingType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('institution_number', models.AutoField(primary_key=True, serialize=False)),
                ('institution_name', models.CharField(db_collation='utf8_general_ci', max_length=50)),
                ('institutional_representative_name', models.CharField(max_length=20)),
                ('institutional_phonenumber', models.CharField(max_length=20)),
                ('institutional_representative_phonenumber', models.CharField(max_length=20)),
                ('institutional_address', models.CharField(max_length=50)),
                ('institutional_representative_mail', models.CharField(max_length=20)),
                ('institutional_type', models.IntegerField()),
                ('program_use', models.IntegerField()),
                ('information_creation_date', models.DateTimeField(blank=True, null=True)),
                ('information_revision_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'institution',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('manager_number', models.AutoField(primary_key=True, serialize=False)),
                ('manager_division', models.CharField(max_length=15)),
                ('manager_position', models.CharField(max_length=15)),
                ('manager_name', models.CharField(max_length=20)),
                ('manager_picture_url', models.CharField(max_length=512)),
                ('manager_phonenumber', models.CharField(max_length=100)),
                ('manager_emergency_phonenumber', models.CharField(max_length=100)),
                ('manager_email', models.CharField(max_length=100)),
                ('information_creation_date', models.DateTimeField(blank=True, null=True)),
                ('information_revision_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'manager',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Manager_Account',
            fields=[
                ('manager_account_number', models.AutoField(primary_key=True, serialize=False)),
                ('manager_id', models.CharField(max_length=30)),
                ('manager_password', models.CharField(max_length=50)),
                ('information_creation_date', models.DateTimeField(blank=True, null=True)),
                ('information_revision_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'manager_account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('notice_number', models.AutoField(primary_key=True, serialize=False)),
                ('notice_title', models.CharField(max_length=100)),
                ('notice_content', models.TextField()),
                ('notice_attachmentlink', models.CharField(db_column='notice_attachmentLink', max_length=1024)),
                ('notice_creationdate', models.DateTimeField(db_column='notice_creationDate')),
                ('notice_updatedate', models.DateTimeField(db_column='notice_updateDate')),
                ('notice_views', models.IntegerField()),
                ('information_creation_date', models.DateTimeField(blank=True, null=True)),
                ('information_revision_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'notice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SoftwareProductFamily',
            fields=[
                ('software_product_family_number', models.AutoField(primary_key=True, serialize=False)),
                ('software_product_family_type', models.CharField(max_length=40)),
                ('software_product_family_name', models.CharField(max_length=40)),
                ('information_creation_date', models.DateTimeField(blank=True, null=True)),
                ('information_revision_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'software_product_family',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SoftwareUpdate',
            fields=[
                ('software_update_number', models.AutoField(primary_key=True, serialize=False)),
                ('software_update_title', models.CharField(max_length=50)),
                ('software_update_content', models.CharField(max_length=1024)),
                ('software_update_creation_date', models.DateTimeField()),
                ('software_update_revision_date', models.DateTimeField()),
                ('information_creation_date', models.DateTimeField(blank=True, null=True)),
                ('information_revision_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'software_update',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StatisticsDate',
            fields=[
                ('statistics_date_number', models.AutoField(primary_key=True, serialize=False)),
                ('contact_date', models.DateField()),
                ('contact_history_count', models.IntegerField()),
                ('information_creation_date', models.DateTimeField(blank=True, null=True)),
                ('information_revision_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'statistics_date',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StatisticsInstitution',
            fields=[
                ('statistics_institution', models.AutoField(primary_key=True, serialize=False)),
                ('contact_history_count', models.IntegerField()),
                ('information_creation_date', models.DateTimeField(blank=True, null=True)),
                ('information_revision_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'statistics_institution',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Statisticsprocessingstage',
            fields=[
                ('statisticsprocessingstage_number', models.AutoField(db_column='statisticsProcessingStage_number', primary_key=True, serialize=False)),
                ('counseling_processing_phase', models.CharField(max_length=10)),
                ('contact_history_count', models.IntegerField()),
                ('information_creation_date', models.DateTimeField(blank=True, null=True)),
                ('information_revision_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'statisticsProcessingStage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StatisticsSoftwareProductFamily',
            fields=[
                ('statistics_software_product_family_number', models.AutoField(primary_key=True, serialize=False)),
                ('contact_history_count', models.IntegerField()),
                ('information_creation_date', models.DateTimeField(blank=True, null=True)),
                ('information_revision_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'statistics_software_product_family',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StatisticsType',
            fields=[
                ('statistics_type', models.AutoField(primary_key=True, serialize=False)),
                ('contact_history_count', models.IntegerField()),
                ('information_creation_date', models.DateTimeField(blank=True, null=True)),
                ('information_revision_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'statistics_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserManagerAccount',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('manager_id', models.CharField(max_length=50)),
                ('manager_password', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'User_manager_account',
                'managed': False,
            },
        ),
    ]
