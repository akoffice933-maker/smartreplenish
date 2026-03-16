# 📤 Инструкция по публикации на GitHub

## Шаг 1: Создайте репозиторий на GitHub

1. Войдите в ваш аккаунт на [GitHub](https://github.com)
2. Нажмите кнопку **"+"** в правом верхнем углу
3. Выберите **"New repository"**
4. Заполните данные:
   - **Repository name**: `smartreplenish`
   - **Description**: "ML-powered demand forecasting and inventory optimization platform"
   - **Visibility**: Public (для инвесторов) или Private (по желанию)
   - **НЕ** инициализируйте репозиторий (README, .gitignore) — они уже есть

5. Нажмите **"Create repository"**

---

## Шаг 2: Привяжите локальный репозиторий к GitHub

В терминале выполните команду (замените `YOUR_USERNAME` на ваш логин GitHub):

```bash
cd d:\SmartReplenish
git remote add origin https://github.com/YOUR_USERNAME/smartreplenish.git
```

Проверьте подключение:

```bash
git remote -v
# Должно вывести:
# origin  https://github.com/YOUR_USERNAME/smartreplenish.git (fetch)
# origin  https://github.com/YOUR_USERNAME/smartreplenish.git (push)
```

---

## Шаг 3: Отправьте код на GitHub

```bash
# Отправка в основную ветку
git push -u origin main

# Или если ветка называется master
git push -u origin master
```

---

## Шаг 4: Настройте GitHub Pages (опционально)

Для демонстрации демо-интерфейса:

1. Перейдите в **Settings** репозитория
2. Выберите **Pages** в левом меню
3. В разделе **Source** выберите:
   - Branch: `main`
   - Folder: `/ (root)`
4. Нажмите **Save**

Через 1-2 минуты демо будет доступно по адресу:
```
https://YOUR_USERNAME.github.io/smartreplenish/smartreplenish_demo.html
```

---

## Шаг 5: Добавьте тему и теги

1. На главной странице репозитория нажмите **"Manage topics"**
2. Добавьте теги:
   - `machine-learning`
   - `forecasting`
   - `supply-chain`
   - `retail`
   - `inventory-optimization`
   - `fastapi`
   - `docker`
   - `python`

---

## Шаг 6: Включите GitHub Actions

1. Перейдите во вкладку **Actions**
2. Если видите предупреждение о необходимости включить workflow, нажмите **"I understand my workflows, go ahead and enable them"**

CI/CD будет запускаться автоматически при каждом push.

---

## Шаг 7: Обновите ссылки в документации

В файлах `README.md` и `INVESTMENT_MEMO.md` замените:

```
https://github.com/your-org/smartreplenish
```

на

```
https://github.com/YOUR_USERNAME/smartreplenish
```

---

## Проверка

После публикации проверьте:

- ✅ Все файлы отображаются на GitHub
- ✅ README.md рендерится корректно
- ✅ GitHub Actions workflow запустился (зелёная галочка)
- ✅ Демо-файл доступен через GitHub Pages

---

## Команды для дальнейшей работы

```bash
# Перед началом работы
git pull origin main

# После внесения изменений
git add .
git commit -m "feat: описание изменений"
git push origin main
```

---

## Приватный репозиторий

Если хотите сделать репозиторий приватным после публикации:

1. **Settings** → **Danger Zone**
2. Нажмите **"Change visibility"**
3. Выберите **"Make private"**
4. Подтвердите действие

---

## Поддержка

Если возникли вопросы:
- [GitHub Docs](https://docs.github.com/)
- [GitHub Community](https://github.community/)
