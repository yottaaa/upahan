from .models import ChatRoom, Message
from django.contrib.auth.models import User

# Create your views here.
def serialized_messages(messages):
	results = []
	for message in messages:
		results.append({
			'id': message.id,
			'room': message.room,
			'sender': message.sender,
			'content': message.content,
			'date_created': message.date_created
		})

	return results

def fetch_messages(data):
	messages = serialized_messages(
		Message.objects.filter(room=data['room']).order_by('-date_created')
	)
	content = {
		'command': 'messages',
		'content': messages
	}
	return content

def new_message(data):
	sender = User.objects.get(username=data['sender'])
	message = Message.objects.create(
		room=data['room'],
		sender=sender,
		content=data['content']
	)
	return 