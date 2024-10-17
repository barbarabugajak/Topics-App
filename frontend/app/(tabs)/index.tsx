import React from 'react';
import { Image, StyleSheet, Platform, View, Text, Button, Pressable, Linking} from 'react-native';
import axios from 'axios';


export default function HomeScreen() {
  const [topic, setTopic] = React.useState(null);
  return (
      <View
        style={{
          flex: 1,
          justifyContent: 'center',
          alignItems: 'center',
        }}>
          {topic &&  
          <>
          <Text style={{
            fontSize: 20,
            marginBottom: 8,
            }}>
              Category: {topic["category"]["name"]}
            </Text>

          {topic["link"] && 
            <Text style={{
              fontSize: 16,
              marginBottom: 8,
              // Make it look like a link
              color: 'blue',
              textDecorationLine: 'underline',
            }}
            onPress={() =>
              Linking.openURL(topic["link"])
            }>
              Link to some information about the topic
            </Text>
          }

          <Text style={{
          fontSize: 24,
          marginBottom: 8,
          // Make bold
          fontWeight: 'bold',
          }}>
            {topic["name"]}
          </Text>
          </>
          }
        <Pressable
          onPress={() => {
            axios.get('http://127.0.0.1:8000/api/random_topic').then((response) => {
              console.log(response.data);
              setTopic(response.data);
            });
          }}
          style={{
            backgroundColor: '#2196F3',
            padding: 10,
            borderRadius: 5,
          }}
        >
          <Text>Choose a{topic && "nother"} random topic</Text>
        </Pressable>
      </View>
    );
}


const styles = StyleSheet.create({
  titleContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  stepContainer: {
    gap: 8,
    marginBottom: 8,
  },
  reactLogo: {
    height: 178,
    width: 290,
    bottom: 0,
    left: 0,
    position: 'absolute',
  },
});
