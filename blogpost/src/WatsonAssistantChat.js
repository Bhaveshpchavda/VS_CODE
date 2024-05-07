import React, { useEffect } from 'react';

const WatsonAssistantChat = () => {
  useEffect(() => {
    // Define Watson Assistant options
    window.watsonAssistantChatOptions = {
      integrationID: "988c654a-c468-43eb-8cae-c79637e65bf7",
      region: "eu-gb",
      serviceInstanceID: "bd74a283-2299-4090-8081-9fa96b9fd719",
      onLoad: async (instance) => { await instance.render(); }
    };

    // Create a script element for Watson Assistant and append it to the document head
    const scriptElement = document.createElement('script');
    scriptElement.src = `https://web-chat.global.assistant.watson.appdomain.cloud/versions/${window.watsonAssistantChatOptions.clientVersion || 'latest'}/WatsonAssistantChatEntry.js`;
    document.head.appendChild(scriptElement);

    // Clean up function to remove the script element when the component is unmounted
    return () => {
      document.head.removeChild(scriptElement);
    };
  }, []);

  return (
    <div id="watson-assistant-chat-container"></div>
  );
};

export default WatsonAssistantChat;
