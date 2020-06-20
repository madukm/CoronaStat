using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace CoronaStat.Models
{
	public class LocationData
	{
		public string Id { get; private set; }
		[Required]
		public string Name { get; set; }

		public DateTime StartDate { get; set; }
		public DateTime EndDate { get; set; }
		//public string ValueType { get; set; } //Obitos, casos recuperados ou casos ativos
		[NotMapped]
		public List<int> Data { get; set; } = new List<int>{ 1, 2, 3, 4 };

		public LocationData()
		{
			Id = Guid.NewGuid().ToString();
		}

		public static List<int> GenerateDateSpan(int beginning, int end)
		{
			List<int> _retList = new List<int>();
			for (int i = beginning; i <= end; i++)
			{
				_retList.Add(i);
			}
			return _retList;
		}
	}
}
