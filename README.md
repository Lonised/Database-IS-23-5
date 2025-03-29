# Список команд для командной строки
Нужен установленный `git`, `Python`, `virtualenv`.

## Переход в папку
```shell
$ cd <путь до папки>

[Вывода нет]
```
где `<путь до папки>` - путь до папки вида "папка_1\папка_2\...".

## Запуск .py файла
```shell
$ python <путь до файла>

[Вывод программы]
```
где `<путь до файла>` - путь до папки вида "папка_1\папка_2\...".

## Создание virtualenv
```shell
$ virtualenv env

created virtual environment CPython3.12.7.final.0-64 in 953ms
  creator CPython3Posix(dest=/media/HDWD220/username/Projects/cursovoi-project-1/env, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, via=copy, app_data_dir=/home/username/.local/share/distrobox-archlinux-devel/.local/share/virtualenv)
    added seed packages: pip==24.2
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
```

## Активация virtualenv
```shell
$ cd env\Scripts\
$ activate
$ cd ..\..
```
**Внимание:** приведен пример активации относительно корневой папки проекта, где находится папка `env`.
## Скачать репозиторий
```shell
$ git clone <ссылка на репозиторий>

Клонирование в «название-репозитория»...
remote: Enumerating objects: 15, done.
remote: Counting objects: 100% (15/15), done.
remote: Compressing objects: 100% (12/12), done.
remote: Total 15 (delta 5), reused 11 (delta 1), pack-reused 0 (from 0)
Получение объектов: 100% (15/15), готово.
Определение изменений: 100% (5/5), готово.
```
где `<ссылка на репозиторий>` - ссылка, который можно получить на домашней странице репозитория по кнопке и копирования ссылки, вроде `https://github.com/dalbsyn/tehnologija-programmirovanija.git`.
## Вывод состояния репозитория
```shell
$ git status

Текущая ветка: master
Эта ветка соответствует «origin/master».

нечего коммитить, нет изменений в рабочем каталоге
```
## Скачать все изменения из удаленного репозитория
```shell
$ git pull

remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0 (from 0)
Распаковка объектов: 100% (3/3), 308 байтов | 308.00 КиБ/с, готово.
Из https://github.com/имя_пользователя/название_репозитория
 * [новая ветка]     master      -> origin/master
Уже актуально.
```
**ВНИМАНИЕ:** это обязательно делать всегда, когда репозиторий скачан не только что, для избежания конфликтов. 
## Вывод веток репозитория
```shell
$ git branch --list

* two
  master
```
Ветка, отмеченная `*` - текущая ветка.
Также возможно посмотреть из вывода команды `git status`, строки `Текущая ветка`.
## Создание ветки репозитория
Командой `checkout`:
```shell
$ git checkout -b название_существующей_ветки

Переключились на новую ветку «название_существующей_ветки»
```
Параметр `-b` - обозначает действие создания ветки.

Командой `branch`:
```shell
$ git branch название_существующей_ветки

[Вывода нет]
```
Разница заключается в том, что первая команда создает и сразу переходит в ветку, а вторая только создает. 
## Смена ветки репозитория
```shell
$ git checkout название_новой_ветки

Переключились на ветку «название_существующей_ветки»
Эта ветка соответствует «origin/название_существующей_ветки».
```
## Добавление измененных файлов
```shell
$ git add файлы

[Вывода нет]
```
Для добавления всех файлов возможно использовать сокращение `.` или `*`.
Возможно также добавить конкретный файл, соответственно перечислив их.
## Сделать `commit`
Если добавить параметр `-m` и далее сообщение, то сразу опубликуется `commit`:
```shell
$ git commit -m "текст"

[two 2757b7a] текст
1 file changed, 1 insertion(+)
create mode 100644 ah.py
```
## Опубликовать изменения
```shell
$ git push

Перечисление объектов: 4, готово.
Подсчет объектов: 100% (4/4), готово.
При сжатии изменений используется до 12 потоков
Сжатие объектов: 100% (2/2), готово.
Запись объектов: 100% (3/3), 353 байта | 353.00 КиБ/с, готово.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/имя_пользователя/название_репозитория
   054bda7..6d7d00b  master -> master
```
Частный случай - вероятнее всего, что если переключиться на свежую ветку, то будет ошибка:
```shell
fatal: The current branch egg has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin название_ветки

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.
```
Достаточно вставить команду выше и все будет работать, то есть `git push --set-upstream origin название_ветки`.
Для того, чтобы происходило автоматически, нужно выполнить следующую команду:
```shell
$ git config push.autoSetupRemote true

[Вывода нет]
```
