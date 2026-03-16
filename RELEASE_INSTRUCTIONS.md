# Инструкция по созданию релиза

## Быстрое создание релиза v1.0.0

### Вариант 1: Через веб-интерфейс (2 минуты)

1. Откройте: https://github.com/akoffice933-maker/smartreplenish/releases/new
2. **Tag version:** выберите `v1.0.0` из списка
3. **Release title:** `v1.0.0 - Initial Release`
4. **Описание:** скопируйте из файла RELEASE_NOTES.md
5. ✅ Поставьте галочку "Set as the latest release"
6. Нажмите **Publish release**

### Вариант 2: Через GitHub CLI

```bash
# Войдите в GitHub
gh auth login

# Создайте релиз
gh release create v1.0.0 ^
  --title "v1.0.0 - Initial Release" ^
  --notes-file RELEASE_NOTES.md ^
  --generate-notes
```

### Вариант 3: Через GitHub API (curl)

```bash
# Замените YOUR_TOKEN на ваш GitHub token
curl -X POST ^
  -H "Authorization: token YOUR_TOKEN" ^
  -H "Accept: application/vnd.github.v3+json" ^
  https://api.github.com/repos/akoffice933-maker/smartreplenish/releases ^
  -d "{\"tag_name\":\"v1.0.0\",\"name\":\"v1.0.0 - Initial Release\",\"body\":\"$(cat RELEASE_NOTES.md)\",\"draft\":false,\"prerelease\":false}"
```

---

## Включение GitHub Pages

1. Откройте: https://github.com/akoffice933-maker/smartreplenish/settings/pages
2. **Source:** Deploy from a branch
3. **Branch:** выберите `main` (или `master`)
4. **Folder:** `/ (root)`
5. Нажмите **Save**

Через 1-2 минуты демо будет доступно по адресу:
```
https://akoffice933-maker.github.io/smartreplenish/smartreplenish_demo.html
```

---

## Проверка

После всех шагов проверьте:

- ✅ Релиз v1.0.0 отображается на https://github.com/akoffice933-maker/smartreplenish/releases
- ✅ GitHub Pages работает (откройте ссылку выше)
- ✅ CI/CD запустился: https://github.com/akoffice933-maker/smartreplenish/actions
