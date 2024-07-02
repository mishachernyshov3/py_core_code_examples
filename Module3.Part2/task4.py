# Проаналізувати логи
logs = """
[2023-10-24 16:32:13,711: INFO/MainProcess] Task adaptive_flow.tasks.task_update_course_extra_data_elements[eae5e1ee-35e3-4efd-ad98-0e0dcc0675fc] received
[2023-10-24 16:32:13,716: ERROR/ForkPoolWorker-1] ************************************************ TASK RUN ************************************
[2023-10-24 16:32:13,753: ERROR/ForkPoolWorker-1] &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&BLOCKS
[2023-10-24 16:32:13,759: ERROR/ForkPoolWorker-1] ['block-v1:RG+CST0001+2023_T2+type@sequential+block@7236d8a4818a47d2b7433b5de17ca68a', 'block-v1:RG+CST0001+2023_T2+type@vertical+block@b00257d3e21646b587474bd9b96a2081']
[2023-10-24 16:32:13,788: ERROR/ForkPoolWorker-1] &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&BLOCKS
Traceback (most recent call last):
  File "/home/misha/.local/share/JetBrains/Toolbox/apps/pycharm-professional/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
  File "<input>", line 1, in <module>
ZeroDivisionError: division by zero
[2023-10-24 16:32:13,791: ERROR/ForkPoolWorker-1] ['block-v1:RG+CST0001+2023_T2+type@sequential+block@7236d8a4818a47d2b7433b5de17ca68a', 'block-v1:RG+CST0001+2023_T2+type@vertical+block@b00257d3e21646b587474bd9b96a2081']
[2023-10-24 16:32:13,793: ERROR/ForkPoolWorker-1] -------------------------------------------current_config.keys()
Traceback (most recent call last):
  File "/home/misha/.local/share/JetBrains/Toolbox/apps/pycharm-professional/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
  File "<input>", line 1, in <module>
TypeError: 'int' object is not subscriptable
[2023-10-24 16:32:13,794: ERROR/ForkPoolWorker-1] dict_keys(['block-v1:RG+CST0001+2023_T2+type@sequential+block@7236d8a4818a47d2b7433b5de17ca68a', 'block-v1:RG+CST0001+2023_T2+type@vertical+block@b00257d3e21646b587474bd9b96a2081'])
[2023-10-24 16:32:13,794: ERROR/ForkPoolWorker-1] -----------------------------------------------course_blocks
[2023-10-24 16:32:13,795: ERROR/ForkPoolWorker-1] ['block-v1:RG+CST0001+2023_T2+type@sequential+block@7236d8a4818a47d2b7433b5de17ca68a', 'block-v1:RG+CST0001+2023_T2+type@vertical+block@b00257d3e21646b587474bd9b96a2081']
[2023-10-24 16:32:13,796: ERROR/ForkPoolWorker-1] set()
Traceback (most recent call last):
  File "/home/misha/.local/share/JetBrains/Toolbox/apps/pycharm-professional/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
  File "<input>", line 1, in <module>
  File "/home/misha/.local/share/JetBrains/Toolbox/apps/pycharm-professional/plugins/python/helpers/pydev/_pydev_bundle/pydev_import_hook.py", line 21, in do_import
    module = self._system_import(name, *args, **kwargs)
ModuleNotFoundError: No module named 'aws_store'
[2023-10-24 16:32:13,802: INFO/ForkPoolWorker-1] Task adaptive_flow.tasks.task_update_course_extra_data_elements[eae5e1ee-35e3-4efd-ad98-0e0dcc0675fc] succeeded in 0.08617439301451668s: None
[2023-10-24 16:32:13,808: INFO/MainProcess] Task cms.djangoapps.contentstore.tasks.update_outline_from_modulestore_task[fe14769e-e082-4415-bd4d-ac66de01e335] received
[2023-10-24 16:32:13,862: INFO/MainProcess] Task openedx.core.djangoapps.discussions.tasks.update_discussions_settings_from_course_task[9e9d7d82-9b81-4f13-9b4a-cba972a7454a] received
[2023-10-24 16:32:13,882: INFO/ForkPoolWorker-1] Replacing CourseOutline for course-v1:RG+CST0001+2023_T2 (version 6537f1798e800e6bc7ac8e82, 1 sequences)
[2023-10-24 16:32:13,907: INFO/ForkPoolWorker-1] Found CourseContext for course-v1:RG+CST0001+2023_T2, updating...
[2023-10-24 16:32:14,040: INFO/ForkPoolWorker-1] Task cms.djangoapps.contentstore.tasks.update_outline_from_modulestore_task[fe14769e-e082-4415-bd4d-ac66de01e335] succeeded in 0.22714334196643904s: None
[2023-10-24 16:32:14,053: INFO/MainProcess] Task openedx.core.djangoapps.bookmarks.tasks.update_xblocks_cache[f4076037-4513-4809-9563-e3b32950396c] received
[2023-10-24 16:32:14,056: INFO/ForkPoolWorker-1] Starting XBlockCaches update for course_key: course-v1:RG+CST0001+2023_T2
[2023-10-24 16:32:14,138: INFO/ForkPoolWorker-1] Ending XBlockCaches update for course_key: course-v1:RG+CST0001+2023_T2
[2023-10-24 16:32:14,140: INFO/ForkPoolWorker-1] Task openedx.core.djangoapps.bookmarks.tasks.update_xblocks_cache[f4076037-4513-4809-9563-e3b32950396c] succeeded in 0.08562918700044975s: None
[2023-10-24 16:32:14,146: INFO/MainProcess] Task openedx.core.djangoapps.course_apps.tasks.update_course_apps_status[19761720-4079-410e-a6ce-99dbbe31811d] received
[2023-10-24 16:32:14,152: INFO/ForkPoolWorker-1] openedx.core.djangoapps.course_apps.tasks.update_course_apps_status[19761720-4079-410e-a6ce-99dbbe31811d]: Caching course apps status for course with id: course-v1:RG+CST0001+2023_T2
[2023-10-24 16:32:14,214: WARNING/ForkPoolWorker-1] Flag 'course_live.enable_course_live' accessed without a request, which is likely in the context of a celery task.
[2023-10-24 16:32:14,226: WARNING/ForkPoolWorker-1] Flag 'teams.enable_teams_app' accessed without a request, which is likely in the context of a celery task.
"""

import re

res = re.findall(r'^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}: (INFO/.*]) .*$', logs, re.MULTILINE)
for k in res:
    print(k)
