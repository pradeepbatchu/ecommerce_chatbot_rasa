# Ecommerce Assiatnat

Rasa install
```bash
rasa init
```
train your nlu model
```bash
rasa train nlu

rasa shell nlu
```
train rasa model
```bash
rasa train
```
Rasa Test:
```bash
rasa test

rasa test nlu -u test/test_data.yml --model models
rasa test core --stories test/test_stories.yml
```
visualize
```bash
rasa visualize
rasa visualize --stories
```
expose model as api
```bash
rasa run --enable-api --endpoints endpoints.yml --cors * --debug --credentials credentials.yml --log-file logs.json
```
Start Action Server
```bash
rasa run actions
```

Test Bot
```bash
payload:

{
  "message": "hi",
  "sender": "Pradeep"
}

Response:

[{
	"recipient_id": "Pradeep",
	"text": "Good to see you! below are quick links for you",
	"buttons": [{
		"title": "Shop By Categories",
		"payload": "\/action_categories_list"
	}, {
		"title": "Show Products",
		"payload": "\/action_customer_product"
	}, {
		"title": "Contact Us",
		"payload": "\/customer_contact"
	}]
}]

```
