import tiktoken

# enc = tiktoken.get_encoding('gpt2')
# print(enc.encode("<FinInstnId><BICFI>CITGUS44TRC</BICFI><Nm>BancFirst</Nm><Ctry>US</Ctry></FinInstnId>"))

enc = tiktoken.get_encoding('cl100k_base_custom')

print(enc.decode(enc.encode("<FinInstnId><BICFI>CITGUS44TRC</BICFI><Nm>BancFirst</Nm><Ctry>US</Ctry></FinInstnId>", allowed_special={'<FinInstnId>', '</FinInstnId>', '<BICFI>', '</BICFI>', '<Nm>', '</Nm>', '<Ctry>', '</Ctry>'})))
