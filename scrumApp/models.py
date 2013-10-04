# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Databasechangelog(models.Model):
    id = models.CharField(max_length=63L, db_column='ID',primary_key=True) # Field name made lowercase.
    author = models.CharField(max_length=63L, db_column='AUTHOR') # Field name made lowercase.
    filename = models.CharField(max_length=200L, db_column='FILENAME') # Field name made lowercase.
    dateexecuted = models.DateTimeField(db_column='DATEEXECUTED') # Field name made lowercase.
    orderexecuted = models.IntegerField(db_column='ORDEREXECUTED') # Field name made lowercase.
    exectype = models.CharField(max_length=10L, db_column='EXECTYPE') # Field name made lowercase.
    md5sum = models.CharField(max_length=35L, db_column='MD5SUM', blank=True) # Field name made lowercase.
    description = models.CharField(max_length=255L, db_column='DESCRIPTION', blank=True) # Field name made lowercase.
    comments = models.CharField(max_length=255L, db_column='COMMENTS', blank=True) # Field name made lowercase.
    tag = models.CharField(max_length=255L, db_column='TAG', blank=True) # Field name made lowercase.
    liquibase = models.CharField(max_length=20L, db_column='LIQUIBASE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'DATABASECHANGELOG'

class Databasechangeloglock(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    locked = models.IntegerField(db_column='LOCKED') # Field name made lowercase.
    lockgranted = models.DateTimeField(null=True, db_column='LOCKGRANTED', blank=True) # Field name made lowercase.
    lockedby = models.CharField(max_length=255L, db_column='LOCKEDBY', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'DATABASECHANGELOGLOCK'

class AcceptanceTest(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    creator = models.ForeignKey('Icescrum2User')
    date_created = models.DateTimeField()
    description = models.TextField(blank=True)
    last_updated = models.DateTimeField()
    name = models.CharField(max_length=255L)
    parent_story = models.ForeignKey('Icescrum2Story')
    uid = models.IntegerField()
    state = models.IntegerField()
    class Meta:
        db_table = 'acceptance_test'

class AclClass(models.Model):
    id = models.BigIntegerField(primary_key=True)
    class_field = models.CharField(max_length=255L, db_column='class') # Field renamed because it was a Python reserved word.
    class Meta:
        db_table = 'acl_class'

class AclEntry(models.Model):
    id = models.BigIntegerField(primary_key=True)
    ace_order = models.IntegerField()
    acl_object_identity = models.ForeignKey('AclObjectIdentity', db_column='acl_object_identity')
    audit_failure = models.TextField() # This field type is a guess.
    audit_success = models.TextField() # This field type is a guess.
    granting = models.TextField() # This field type is a guess.
    mask = models.IntegerField()
    sid = models.ForeignKey('AclSid', db_column='sid')
    class Meta:
        db_table = 'acl_entry'

class AclObjectIdentity(models.Model):
    id = models.BigIntegerField(primary_key=True)
    object_id_class = models.ForeignKey(AclClass, db_column='object_id_class')
    entries_inheriting = models.TextField() # This field type is a guess.
    object_id_identity = models.BigIntegerField()
    owner_sid = models.ForeignKey('AclSid', null=True, db_column='owner_sid', blank=True)
    parent_object = models.ForeignKey('self', null=True, db_column='parent_object', blank=True)
    class Meta:
        db_table = 'acl_object_identity'

class AclSid(models.Model):
    id = models.BigIntegerField(primary_key=True)
    principal = models.TextField() # This field type is a guess.
    sid = models.CharField(max_length=255L)
    class Meta:
        db_table = 'acl_sid'

class AttachmentableAttachment(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    content_type = models.CharField(max_length=255L, blank=True)
    date_created = models.DateTimeField()
    ext = models.CharField(max_length=255L, blank=True)
    input_name = models.CharField(max_length=255L)
    length = models.BigIntegerField()
    name = models.CharField(max_length=255L)
    poster_class = models.CharField(max_length=255L)
    poster_id = models.BigIntegerField()
    provider = models.CharField(max_length=255L, blank=True)
    url = models.TextField(blank=True)
    class Meta:
        db_table = 'attachmentable_attachment'

class AttachmentableAttachmentlink(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    attachment = models.ForeignKey(AttachmentableAttachment)
    attachment_ref = models.BigIntegerField()
    attachment_ref_class = models.CharField(max_length=255L)
    type = models.CharField(max_length=255L)
    class Meta:
        db_table = 'attachmentable_attachmentlink'

class Authority(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    authority = models.CharField(max_length=255L, unique=True)
    class Meta:
        db_table = 'authority'

class BiImages(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    data = models.TextField()
    type = models.CharField(max_length=255L)
    class Meta:
        db_table = 'bi_images'

class Comment(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    body = models.TextField()
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    poster_class = models.CharField(max_length=255L)
    poster_id = models.BigIntegerField()
    class Meta:
        db_table = 'comment'

class CommentLink(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    comment = models.ForeignKey(Comment)
    comment_ref = models.BigIntegerField()
    type = models.CharField(max_length=255L)
    class Meta:
        db_table = 'comment_link'

class FluxiableActivity(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    cached_description = models.TextField(blank=True)
    cached_id = models.BigIntegerField()
    cached_label = models.TextField()
    code = models.CharField(max_length=255L)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    poster_class = models.CharField(max_length=255L)
    poster_id = models.BigIntegerField()
    class Meta:
        db_table = 'fluxiable_activity'

class FluxiableActivityLink(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    activity = models.ForeignKey(FluxiableActivity)
    activity_ref = models.BigIntegerField()
    type = models.CharField(max_length=255L)
    class Meta:
        db_table = 'fluxiable_activity_link'

class FollowLink(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    follow_ref = models.BigIntegerField()
    follower_class = models.CharField(max_length=255L)
    follower_id = models.BigIntegerField()
    type = models.CharField(max_length=255L)
    class Meta:
        db_table = 'follow_link'

class Icescrum2Actor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    backlog = models.ForeignKey('Icescrum2Product')
    creation_date = models.DateTimeField()
    date_created = models.DateTimeField()
    description = models.TextField(blank=True)
    expertness_level = models.IntegerField()
    instances = models.IntegerField()
    last_updated = models.DateTimeField()
    name = models.CharField(max_length=100L)
    notes = models.TextField(blank=True)
    satisfaction_criteria = models.CharField(max_length=255L, blank=True)
    uid = models.BigIntegerField()
    use_frequency = models.IntegerField()
    class Meta:
        db_table = 'icescrum2_actor'

class Icescrum2Cliches(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    data = models.TextField()
    date_prise = models.DateTimeField()
    parent_time_box = models.ForeignKey('Icescrum2Timebox')
    type = models.IntegerField()
    class Meta:
        db_table = 'icescrum2_cliches'

class Icescrum2Domain(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    backlog = models.ForeignKey('Icescrum2Product')
    color = models.CharField(max_length=255L)
    creation_date = models.DateTimeField()
    date_created = models.DateTimeField()
    description = models.TextField(blank=True)
    last_updated = models.DateTimeField()
    name = models.CharField(max_length=100L)
    notes = models.TextField(blank=True)
    publish = models.TextField() # This field type is a guess.
    text_color = models.CharField(max_length=255L)
    uid = models.IntegerField()
    class Meta:
        db_table = 'icescrum2_domain'

class Icescrum2Feature(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    backlog = models.ForeignKey('Icescrum2Product')
    color = models.CharField(max_length=255L)
    creation_date = models.DateTimeField()
    date_created = models.DateTimeField()
    description = models.TextField(blank=True)
    last_updated = models.DateTimeField()
    name = models.CharField(max_length=100L)
    notes = models.TextField(blank=True)
    parent_domain = models.ForeignKey(Icescrum2Domain, null=True, blank=True)
    rank = models.IntegerField()
    type = models.IntegerField()
    uid = models.BigIntegerField()
    value = models.IntegerField(null=True, blank=True)
    parent_release = models.ForeignKey('Icescrum2Release', null=True, blank=True)
    class Meta:
        db_table = 'icescrum2_feature'

class Icescrum2Impediment(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    backlog = models.ForeignKey('Icescrum2Product')
    creation_date = models.DateTimeField()
    creator = models.ForeignKey('Icescrum2User')
    date_close = models.DateTimeField(null=True, blank=True)
    date_created = models.DateTimeField()
    date_open = models.DateTimeField()
    description = models.TextField(blank=True)
    impact = models.TextField()
    last_updated = models.DateTimeField()
    name = models.CharField(max_length=100L)
    notes = models.TextField(blank=True)
    rank = models.IntegerField(null=True, blank=True)
    solution = models.TextField()
    state = models.IntegerField()
    uid = models.IntegerField()
    class Meta:
        db_table = 'icescrum2_impediment'

class Icescrum2Product(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200L, blank=True)
    pkey = models.CharField(max_length=10L, blank=True)
    planning_poker_game_type = models.IntegerField(null=True, blank=True)
    preferences = models.ForeignKey('Icescrum2ProductPreferences', null=True, blank=True)
    class Meta:
        db_table = 'icescrum2_product'

class Icescrum2ProductPreferences(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    archived = models.IntegerField()
    assign_on_begin_task = models.TextField() # This field type is a guess.
    assign_on_create_task = models.TextField() # This field type is a guess.
    auto_create_task_on_empty_story = models.TextField() # This field type is a guess.
    auto_done_story = models.TextField() # This field type is a guess.
    daily_meeting_hour = models.CharField(max_length=255L)
    display_recurrent_tasks = models.TextField() # This field type is a guess.
    display_urgent_tasks = models.TextField() # This field type is a guess.
    estimated_sprints_duration = models.IntegerField()
    hidden = models.TextField() # This field type is a guess.
    hide_weekend = models.IntegerField()
    limit_urgent_tasks = models.IntegerField()
    no_estimation = models.TextField() # This field type is a guess.
    release_planning_hour = models.CharField(max_length=255L)
    sprint_planning_hour = models.CharField(max_length=255L)
    sprint_retrospective_hour = models.CharField(max_length=255L)
    sprint_review_hour = models.CharField(max_length=255L)
    timezone = models.CharField(max_length=255L)
    url = models.CharField(max_length=255L, blank=True)
    webservices = models.IntegerField()
    stake_holder_restricted_views = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'icescrum2_product_preferences'

class Icescrum2ProductTeams(models.Model):
    team = models.ForeignKey('Icescrum2Team')
    product = models.ForeignKey(Icescrum2Product)
    class Meta:
        db_table = 'icescrum2_product_teams'

class Icescrum2Release(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255L, blank=True)
    parent_product = models.ForeignKey(Icescrum2Product, null=True, blank=True)
    release_velocity = models.FloatField(null=True, blank=True)
    state = models.IntegerField(null=True, blank=True)
    vision = models.TextField(blank=True)
    class Meta:
        db_table = 'icescrum2_release'

class Icescrum2Sprint(models.Model):
    id = models.BigIntegerField(primary_key=True)
    activation_date = models.DateTimeField(null=True, blank=True)
    capacity = models.FloatField(null=True, blank=True)
    close_date = models.DateTimeField(null=True, blank=True)
    daily_work_time = models.FloatField(null=True, blank=True)
    done_definition = models.TextField(blank=True)
    parent_release = models.ForeignKey(Icescrum2Release, null=True, blank=True)
    retrospective = models.TextField(blank=True)
    state = models.IntegerField(null=True, blank=True)
    velocity = models.FloatField(null=True, blank=True)
    delivered_version = models.CharField(max_length=255L, blank=True)
    initial_remaining_time = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = 'icescrum2_sprint'

class Icescrum2Story(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    accepted_date = models.DateTimeField(null=True, blank=True)
    actor = models.ForeignKey(Icescrum2Actor, null=True, blank=True)
    affect_version = models.CharField(max_length=255L, blank=True)
    backlog = models.ForeignKey(Icescrum2Product)
    creation_date = models.DateTimeField()
    creator = models.ForeignKey('Icescrum2User', null=True, blank=True)
    date_created = models.DateTimeField()
    description = models.TextField(blank=True)
    done_date = models.DateTimeField(null=True, blank=True)
    effort = models.IntegerField(null=True, blank=True)
    estimated_date = models.DateTimeField(null=True, blank=True)
    execution_frequency = models.IntegerField()
    feature = models.ForeignKey(Icescrum2Feature, null=True, blank=True)
    in_progress_date = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField()
    name = models.CharField(max_length=100L)
    notes = models.TextField(blank=True)
    origin = models.CharField(max_length=255L, blank=True)
    parent_sprint = models.ForeignKey(Icescrum2Sprint, null=True, blank=True)
    planned_date = models.DateTimeField(null=True, blank=True)
    rank = models.IntegerField()
    state = models.IntegerField()
    suggested_date = models.DateTimeField(null=True, blank=True)
    text_as = models.TextField(blank=True)
    textican = models.TextField(blank=True)
    text_to = models.TextField(blank=True)
    type = models.IntegerField()
    uid = models.BigIntegerField()
    value = models.IntegerField()
    depends_on = models.ForeignKey('self', null=True, blank=True)
    class Meta:
        db_table = 'icescrum2_story'

class Icescrum2Task(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    backlog = models.ForeignKey(Icescrum2Sprint)
    blocked = models.IntegerField()
    color = models.CharField(max_length=255L, blank=True)
    creation_date = models.DateTimeField()
    creator = models.ForeignKey('Icescrum2User',related_name="created_tasks")
    date_created = models.DateTimeField()
    description = models.TextField(blank=True)
    done_date = models.DateTimeField(null=True, blank=True)
    estimation = models.FloatField(null=True, blank=True)
    impediment = models.ForeignKey(Icescrum2Impediment, null=True, blank=True)
    in_progress_date = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField()
    name = models.CharField(max_length=100L)
    notes = models.TextField(blank=True)
    parent_story = models.ForeignKey(Icescrum2Story, null=True, blank=True)
    rank = models.IntegerField()
    responsible = models.ForeignKey('Icescrum2User', null=True, blank=True,related_name="my_tasks")
    state = models.IntegerField()
    type = models.IntegerField(null=True, blank=True)
    uid = models.BigIntegerField()
    initial = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = 'icescrum2_task'

class Icescrum2TaskIcescrum2User(models.Model):
    task_participants = models.ForeignKey(Icescrum2Task, null=True, blank=True)
    user = models.ForeignKey('Icescrum2User', null=True, blank=True)
    class Meta:
        db_table = 'icescrum2_task_icescrum2_user'

class Icescrum2Team(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    description = models.TextField(blank=True)
    last_updated = models.DateTimeField()
    name = models.CharField(max_length=255L, unique=True)
    preferences = models.ForeignKey('Icescrum2TeamPreferences')
    uid = models.CharField(max_length=255L)
    velocity = models.IntegerField()
    class Meta:
        db_table = 'icescrum2_team'

class Icescrum2TeamMembers(models.Model):
    team = models.ForeignKey(Icescrum2Team)
    user = models.ForeignKey('Icescrum2User')
    class Meta:
        db_table = 'icescrum2_team_members'

class Icescrum2TeamPreferences(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    allow_new_members = models.TextField() # This field type is a guess.
    class Meta:
        db_table = 'icescrum2_team_preferences'

class Icescrum2Timebox(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    description = models.TextField(blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    goal = models.TextField(blank=True)
    last_updated = models.DateTimeField()
    order_number = models.IntegerField()
    start_date = models.DateTimeField()
    class Meta:
        db_table = 'icescrum2_timebox'

class Icescrum2User(models.Model):
    list_display = ('username','email','first_name', 'last_name')
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    account_expired = models.TextField() # This field type is a guess.
    account_external = models.IntegerField()
    account_locked = models.TextField() # This field type is a guess.
    date_created = models.DateTimeField()
    email = models.CharField(max_length=255L)
    enabled = models.TextField() # This field type is a guess.
    first_name = models.CharField(max_length=255L)
    last_name = models.CharField(max_length=255L)
    last_updated = models.DateTimeField()
    passwd = models.CharField(max_length=255L)
    password_expired = models.TextField() # This field type is a guess.
    preferences = models.ForeignKey('Icescrum2UserPreferences')
    uid = models.CharField(max_length=255L)
    username = models.CharField(max_length=255L)
    class Meta:
        db_table = 'icescrum2_user'

class Icescrum2UserPreferences(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    activity = models.CharField(max_length=255L, blank=True)
    filter_task = models.CharField(max_length=255L)
    hide_done_state = models.IntegerField()
    language = models.CharField(max_length=255L)
    last_product_opened = models.CharField(max_length=255L, blank=True)
    emails_settings_data = models.TextField(blank=True)
    class Meta:
        db_table = 'icescrum2_user_preferences'

class Icescrum2UserPreferencesMenu(models.Model):
    menu = models.BigIntegerField(null=True, blank=True)
    menu_idx = models.CharField(max_length=255L, blank=True)
    menu_elt = models.CharField(max_length=255L)
    class Meta:
        db_table = 'icescrum2_user_preferences_menu'

class Icescrum2UserPreferencesMenuHidden(models.Model):
    menu_hidden = models.BigIntegerField(null=True, blank=True)
    menu_hidden_idx = models.CharField(max_length=255L, blank=True)
    menu_hidden_elt = models.CharField(max_length=255L)
    class Meta:
        db_table = 'icescrum2_user_preferences_menu_hidden'

class TagLinks(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    tag = models.ForeignKey('Tags')
    tag_ref = models.BigIntegerField()
    type = models.CharField(max_length=255L)
    class Meta:
        db_table = 'tag_links'

class Tags(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    name = models.CharField(max_length=255L, unique=True)
    class Meta:
        db_table = 'tags'

class TestFollowable(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    name = models.CharField(max_length=255L)
    class Meta:
        db_table = 'test_followable'

class TestFollower(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    name = models.CharField(max_length=255L)
    class Meta:
        db_table = 'test_follower'

class TestReport(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    name = models.CharField(max_length=255L)
    class Meta:
        db_table = 'test_report'

class Testbfollowable(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    name = models.CharField(max_length=255L)
    class Meta:
        db_table = 'testbfollowable'

class UserAuthority(models.Model):
    authority = models.ForeignKey(Authority)
    user = models.ForeignKey(Icescrum2User)
    class Meta:
        db_table = 'user_authority'

