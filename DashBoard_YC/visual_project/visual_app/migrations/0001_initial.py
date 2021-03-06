# Generated by Django 2.1.5 on 2019-01-17 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ifm_loan_appl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_appl_id', models.IntegerField(unique=True, verbose_name='appr_id')),
                ('item_code', models.CharField(max_length=50, null=True, verbose_name='用户手机号')),
                ('status', models.CharField(max_length=50, null=True, verbose_name='用户状态')),
                ('loaning_status', models.CharField(max_length=50, null=True)),
                ('create_date', models.DateTimeField(null=True, verbose_name='申请时间')),
                ('prvince', models.CharField(max_length=50, null=True, verbose_name='群体')),
                ('city', models.CharField(max_length=500, null=True, verbose_name='下载来源')),
                ('comment', models.TextField(max_length=2048, null=True, verbose_name='补充情况')),
                ('update_time', models.DateTimeField(null=True, verbose_name='最近提交借款时间')),
                ('credit_amt', models.CharField(max_length=50, null=True, verbose_name='授信额度')),
                ('level', models.CharField(max_length=50, null=True, verbose_name='信用等级')),
                ('user_id', models.IntegerField(null=True, verbose_name='用户id')),
                ('zhima_credit_score', models.CharField(max_length=50, null=True, verbose_name='芝麻分')),
                ('zhima_ivs_score', models.CharField(max_length=500, null=True, verbose_name='反欺诈')),
                ('watchlistii_is_matched', models.CharField(max_length=50, null=True, verbose_name='是否是行业关注名单')),
                ('invite_code', models.CharField(max_length=255, null=True, verbose_name='邀请码')),
                ('inviter_invite_code', models.CharField(max_length=255, null=True, verbose_name='邀请人邀请码')),
                ('authen_time', models.DateTimeField(null=True, verbose_name='认证时间')),
                ('operator_status', models.CharField(max_length=32, null=True, verbose_name='运营商状态')),
                ('zhima_status', models.CharField(max_length=32, null=True, verbose_name='芝麻分状态')),
                ('base_info_status', models.CharField(max_length=32, null=True, verbose_name='风控拒绝基本信息状态')),
                ('contact_info_status', models.CharField(max_length=32, null=True, verbose_name='风控拒绝联系人状态')),
                ('account_status', models.IntegerField(null=True, verbose_name='账户状态')),
                ('abnormal_number', models.IntegerField(default='0', null=True, verbose_name='异常次数')),
                ('upgrade_account_time', models.DateTimeField(null=True, verbose_name='账户升级时间')),
                ('recover_account_time', models.DateTimeField(null=True, verbose_name='账户恢复正常时间')),
                ('active_sign', models.CharField(max_length=4, null=True, verbose_name='奖励标记')),
                ('ssq_apply_status', models.CharField(max_length=4, null=True, verbose_name='上上签用户申请状态')),
                ('mark', models.CharField(max_length=50, null=True, verbose_name='用户提额标签')),
                ('lift_mark', models.CharField(max_length=255, null=True, verbose_name='用户提额标签')),
                ('level_mark', models.CharField(max_length=255, null=True, verbose_name='用户提等标签')),
                ('type', models.IntegerField(null=True, verbose_name='用户类型')),
            ],
            options={
                'verbose_name_plural': '莫愁花用户注册表',
                'db_table': 'ifm_loan_appl',
                'ordering': ['create_date', 'city'],
            },
        ),
        migrations.CreateModel(
            name='qsh_loan_appl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_appl_id', models.IntegerField(unique=True, verbose_name='appr_id')),
                ('item_code', models.CharField(max_length=50, null=True, verbose_name='用户手机号')),
                ('status', models.CharField(max_length=50, null=True, verbose_name='用户状态')),
                ('loaning_status', models.CharField(max_length=50, null=True)),
                ('create_date', models.DateTimeField(null=True, verbose_name='申请时间')),
                ('prvince', models.CharField(max_length=50, null=True, verbose_name='群体')),
                ('city', models.CharField(max_length=500, null=True, verbose_name='下载来源')),
                ('comment', models.TextField(max_length=2048, null=True, verbose_name='补充情况')),
                ('update_time', models.DateTimeField(null=True, verbose_name='最近提交借款时间')),
                ('credit_amt', models.CharField(max_length=50, null=True, verbose_name='授信额度')),
                ('level', models.CharField(max_length=50, null=True, verbose_name='信用等级')),
                ('user_id', models.IntegerField(null=True, verbose_name='用户id')),
                ('zhima_credit_score', models.CharField(max_length=50, null=True, verbose_name='芝麻分')),
                ('zhima_ivs_score', models.CharField(max_length=500, null=True, verbose_name='反欺诈')),
                ('watchlistii_is_matched', models.CharField(max_length=50, null=True, verbose_name='是否是行业关注名单')),
                ('invite_code', models.CharField(max_length=255, null=True, verbose_name='邀请码')),
                ('inviter_invite_code', models.CharField(max_length=255, null=True, verbose_name='邀请人邀请码')),
                ('authen_time', models.DateTimeField(null=True, verbose_name='认证时间')),
                ('operator_status', models.CharField(max_length=32, null=True, verbose_name='运营商状态')),
                ('zhima_status', models.CharField(max_length=32, null=True, verbose_name='芝麻分状态')),
                ('base_info_status', models.CharField(max_length=32, null=True, verbose_name='风控拒绝基本信息状态')),
                ('contact_info_status', models.CharField(max_length=32, null=True, verbose_name='风控拒绝联系人状态')),
                ('account_status', models.IntegerField(null=True, verbose_name='账户状态')),
                ('abnormal_number', models.IntegerField(default='0', null=True, verbose_name='异常次数')),
                ('upgrade_account_time', models.DateTimeField(null=True, verbose_name='账户升级时间')),
                ('recover_account_time', models.DateTimeField(null=True, verbose_name='账户恢复正常时间')),
                ('active_sign', models.CharField(max_length=4, null=True, verbose_name='奖励标记')),
                ('ssq_apply_status', models.CharField(max_length=4, null=True, verbose_name='上上签用户申请状态')),
            ],
            options={
                'verbose_name_plural': '现金树用户注册表',
                'db_table': 'qsh_loan_appl',
                'ordering': ['create_date', 'city'],
            },
        ),
        migrations.CreateModel(
            name='sxh_loan_appl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_appl_id', models.IntegerField(unique=True, verbose_name='appr_id')),
                ('item_code', models.CharField(max_length=50, null=True, verbose_name='用户手机号')),
                ('status', models.CharField(max_length=50, null=True, verbose_name='用户状态')),
                ('loaning_status', models.CharField(max_length=50, null=True)),
                ('create_date', models.DateTimeField(null=True, verbose_name='申请时间')),
                ('prvince', models.CharField(max_length=50, null=True, verbose_name='群体')),
                ('city', models.CharField(max_length=500, null=True, verbose_name='下载来源')),
                ('comment', models.TextField(max_length=2048, null=True, verbose_name='补充情况')),
                ('update_time', models.DateTimeField(null=True, verbose_name='最近提交借款时间')),
                ('credit_amt', models.CharField(max_length=50, null=True, verbose_name='授信额度')),
                ('level', models.CharField(max_length=50, null=True, verbose_name='信用等级')),
                ('user_id', models.IntegerField(null=True, verbose_name='用户id')),
                ('zhima_credit_score', models.CharField(max_length=50, null=True, verbose_name='芝麻分')),
                ('zhima_ivs_score', models.CharField(max_length=500, null=True, verbose_name='反欺诈')),
                ('watchlistii_is_matched', models.CharField(max_length=50, null=True, verbose_name='是否是行业关注名单')),
                ('invite_code', models.CharField(max_length=255, null=True, verbose_name='邀请码')),
                ('inviter_invite_code', models.CharField(max_length=255, null=True, verbose_name='邀请人邀请码')),
                ('authen_time', models.DateTimeField(null=True, verbose_name='认证时间')),
                ('operator_status', models.CharField(max_length=32, null=True, verbose_name='运营商状态')),
                ('zhima_status', models.CharField(max_length=32, null=True, verbose_name='芝麻分状态')),
                ('base_info_status', models.CharField(max_length=32, null=True, verbose_name='风控拒绝基本信息状态')),
                ('contact_info_status', models.CharField(max_length=32, null=True, verbose_name='风控拒绝联系人状态')),
                ('account_status', models.IntegerField(null=True, verbose_name='账户状态')),
                ('abnormal_number', models.IntegerField(default='0', null=True, verbose_name='异常次数')),
                ('upgrade_account_time', models.DateTimeField(null=True, verbose_name='账户升级时间')),
                ('recover_account_time', models.DateTimeField(null=True, verbose_name='账户恢复正常时间')),
                ('active_sign', models.CharField(max_length=4, null=True, verbose_name='奖励标记')),
                ('ssq_apply_status', models.CharField(max_length=4, null=True, verbose_name='上上签用户申请状态')),
                ('app_type', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': '随薪花用户注册表',
                'db_table': 'sxh_loan_appl',
                'ordering': ['create_date', 'city'],
            },
        ),
        migrations.CreateModel(
            name='tty_loan_appl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_appl_id', models.IntegerField(unique=True, verbose_name='appr_id')),
                ('item_code', models.CharField(max_length=50, null=True, verbose_name='用户手机号')),
                ('status', models.CharField(max_length=50, null=True, verbose_name='用户状态')),
                ('loaning_status', models.CharField(max_length=50, null=True)),
                ('create_date', models.DateTimeField(null=True, verbose_name='申请时间')),
                ('prvince', models.CharField(max_length=50, null=True, verbose_name='群体')),
                ('city', models.CharField(max_length=500, null=True, verbose_name='下载来源')),
                ('comment', models.TextField(max_length=2048, null=True, verbose_name='补充情况')),
                ('update_time', models.DateTimeField(null=True, verbose_name='最近提交借款时间')),
                ('credit_amt', models.CharField(max_length=50, null=True, verbose_name='授信额度')),
                ('level', models.CharField(max_length=50, null=True, verbose_name='信用等级')),
                ('user_id', models.IntegerField(null=True, verbose_name='用户id')),
                ('zhima_credit_score', models.CharField(max_length=50, null=True, verbose_name='芝麻分')),
                ('zhima_ivs_score', models.CharField(max_length=500, null=True, verbose_name='反欺诈')),
                ('watchlistii_is_matched', models.CharField(max_length=50, null=True, verbose_name='是否是行业关注名单')),
                ('invite_code', models.CharField(max_length=255, null=True, verbose_name='邀请码')),
                ('inviter_invite_code', models.CharField(max_length=255, null=True, verbose_name='邀请人邀请码')),
                ('authen_time', models.DateTimeField(null=True, verbose_name='认证时间')),
                ('operator_status', models.CharField(max_length=32, null=True, verbose_name='运营商状态')),
                ('zhima_status', models.CharField(max_length=32, null=True, verbose_name='芝麻分状态')),
                ('base_info_status', models.CharField(max_length=32, null=True, verbose_name='风控拒绝基本信息状态')),
                ('contact_info_status', models.CharField(max_length=32, null=True, verbose_name='风控拒绝联系人状态')),
                ('account_status', models.IntegerField(null=True, verbose_name='账户状态')),
                ('abnormal_number', models.IntegerField(default='0', null=True, verbose_name='异常次数')),
                ('upgrade_account_time', models.DateTimeField(null=True, verbose_name='账户升级时间')),
                ('recover_account_time', models.DateTimeField(null=True, verbose_name='账户恢复正常时间')),
                ('active_sign', models.CharField(max_length=4, null=True, verbose_name='奖励标记')),
                ('ssq_apply_status', models.CharField(max_length=4, null=True, verbose_name='上上签用户申请状态')),
                ('mark', models.CharField(max_length=50, null=True, verbose_name='用户提额标签')),
                ('lift_mark', models.CharField(max_length=255, null=True, verbose_name='用户提额标签')),
                ('level_mark', models.CharField(max_length=255, null=True, verbose_name='用户提等标签')),
                ('type', models.IntegerField(null=True, verbose_name='用户类型')),
                ('app_type', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': '一万元用户注册表',
                'db_table': 'tty_loan_appl',
                'ordering': ['create_date', 'city'],
            },
        ),
    ]
